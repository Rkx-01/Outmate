from abc import ABC, abstractmethod
from typing import Any, Dict, List, Optional
import json, re, os, asyncio, logging
from agno.agent import Agent
from agno.models.google import Gemini
from agno.db.sqlite.sqlite import SqliteDb
from models.agents import AgentInput, AgentOutput
from memory.mempalace import mempalace_diary_write, mempalace_search
from utils.api_keys import key_manager
from config import VALID_LINKEDIN_CATEGORIES

log = logging.getLogger(__name__)
_DB_FILE = os.path.join(os.path.dirname(__file__), "..", "data", "gtm_agent_sessions.db")

# Model rotation order for error recovery
MODEL_ROTATION = [
    "gemini-3.1-flash-lite-preview",  # Primary (already tried 3x)
    "gemini-3-flash-preview",          # Secondary  
    "gemini-3.1-pro-preview",          # Tertiary
]

# Error message for exhausted attempts
RATE_LIMIT_ERROR_MESSAGE = """Rate limit exceeded across all models and API keys. The task could not be completed. You can click Restart to try the entire job again or Resume to continue from where it left off."""


async def arun_with_backoff(agent, prompt: str, max_retries_per_model: int = 3):
    """
    Call agent.arun with model rotation on rate limit errors.
    
    Strategy: Try each model up to 3 times with different API keys.
    Total attempts: 3 models × 3 keys = 9 attempts maximum.
    If all fail, return specific error message for frontend.
    """
    log.info(
        f"[gemini] [{agent.name}] prompt ({len(prompt)} chars):\n"
        f"{'─' * 60}\n{prompt.strip()}\n{'─' * 60}"
    )
    
    total_attempts = 0
    max_total_attempts = len(MODEL_ROTATION) * max_retries_per_model  # 9 attempts
    model_index = 0
    
    while total_attempts < max_total_attempts:
        current_model = MODEL_ROTATION[model_index]
        attempt_in_model = total_attempts % max_retries_per_model
        
        try:
            # Switch to new model if needed
            if agent.model.id != current_model:
                new_key = key_manager.get_next_key()
                agent.model = Gemini(id=current_model, api_key=new_key)
                log.warning(f"[{agent.name}] Switching to model: {current_model}")
            
            # Rotate API key for each retry
            if attempt_in_model > 0:
                new_key = key_manager.get_next_key()
                agent.model.api_key = new_key
                log.info(f"[{agent.name}] Rotating API key for {current_model} (attempt {attempt_in_model + 1})")
            
            response = await agent.arun(prompt)
            content_str = getattr(response, 'content', str(response))
            
            # Detect swallowed API errors by Agno
            if '"error"' in content_str and any(x in content_str for x in ['"code": 503', '"code": 429', '"status": "UNAVAILABLE"']):
                raise ValueError(f"Agno API Swallowed Error: {content_str[:150]}")
            
            # Success - return response
            log.info(
                f"[gemini] [{agent.name}] response (attempt {total_attempts + 1}):\n"
                f"{'─' * 60}\n{content_str}\n{'─' * 60}"
            )
            return response
            
        except Exception as e:
            error_str = str(e).lower()
            total_attempts += 1
            
            # Check if error is rate limit or service overload
            is_rate_limit_error = any(x in error_str for x in [
                "429", "503", "quota", "rate", "resource_exhausted", 
                "unavailable", "service unavailable", "high demand",
                "overloaded"
            ])
            
            if is_rate_limit_error and total_attempts < max_total_attempts:
                # Move to next model if exhausted retries for current model
                if (attempt_in_model + 1) >= max_retries_per_model:
                    model_index = (model_index + 1) % len(MODEL_ROTATION)
                
                wait = 2 ** attempt_in_model  # 1s, 2s, 4s
                log.warning(
                    f"[{agent.name}] Rate limit error on {current_model} (attempt {total_attempts}/{max_total_attempts}): {error_str[:80]}. "
                    f"Retrying in {wait}s..."
                )
                await asyncio.sleep(wait)
                continue
            
            elif not is_rate_limit_error:
                # Non-retryable error - fail immediately
                log.error(f"[{agent.name}] Non-retryable error on attempt {total_attempts}: {e}")
                raise
            
            else:
                # All attempts exhausted
                log.error(f"[{agent.name}] All {max_total_attempts} attempts exhausted across models. Final error: {e}")
                break
    
    # All attempts failed - return rate limit error for frontend
    error_output = {
        "error": RATE_LIMIT_ERROR_MESSAGE,
        "attempt_count": total_attempts,
        "models_tried": MODEL_ROTATION,
        "recommendation": "User can click Restart or Resume"
    }
    raise Exception(json.dumps(error_output))


def parse_llm_json(content: str) -> dict:
    """Extract JSON from Agno agent response content string, handling markdown fences."""
    if not content:
        raise ValueError("Empty content received from LLM")

    text = re.sub(r'^\s*```json\s*', '', content, flags=re.MULTILINE)
    text = re.sub(r'```\s*$', '', text, flags=re.MULTILINE)
    text = text.strip()

    match = re.search(r'(\{.*\}|\[.*\])', text, re.DOTALL)
    if match:
        return json.loads(match.group(1))
    raise ValueError(f"No JSON found in LLM response: {text[:200]}")


class BaseGTMAgent(ABC):
    # Valid LinkedIn industry categories for filtering and validation
    VALID_LINKEDIN_CATEGORIES = VALID_LINKEDIN_CATEGORIES
    
    def __init__(self, name: str, description: str, tools: List[Any] = None, instructions: List[str] = None, use_tools: bool = True):
        self.name = name
        self.description = description
        self.use_tools = use_tools
        self.default_tools = [mempalace_diary_write, mempalace_search] if use_tools else []
        self.tools = self.default_tools + (tools or [])
        self.instructions = instructions or []

        self.agent = Agent(
            name=self.name,
            description=self.description,
            model=Gemini(id=MODEL_ROTATION[0], api_key=key_manager.get_key()),
            tools=self.tools,
            instructions=self.instructions + [
                "Always return your final answer in the requested JSON format."
            ],
            markdown=True,
            add_history_to_context=True,
            db=SqliteDb(db_file=_DB_FILE),
        )

    @abstractmethod
    async def run(self, input_data: AgentInput) -> AgentOutput:
        pass


class AgentRegistry:
    _agents: Dict[str, BaseGTMAgent] = {}

    @classmethod
    def register(cls, agent: BaseGTMAgent):
        cls._agents[agent.name] = agent

    @classmethod
    def get_agent(cls, name: str) -> Optional[BaseGTMAgent]:
        return cls._agents.get(name)

    @classmethod
    def list_agents(cls) -> List[BaseGTMAgent]:
        return list(cls._agents.values())