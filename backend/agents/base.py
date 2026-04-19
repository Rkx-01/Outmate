from abc import ABC, abstractmethod
from typing import Any, Dict, List, Optional
import json, re, os, asyncio, logging
from agno.agent import Agent
try:
    from agno.models.groq import Groq
    from agno.models.base import Model
    MOCK_MODE = False
except ImportError:
    print("WARNING: Groq model failed to load. Running in MOCK MODE.")
    MOCK_MODE = True
    Groq = lambda **kwargs: None
    Model = object
from agno.db.sqlite.sqlite import SqliteDb
from models.agents import AgentInput, AgentOutput
from memory.mempalace import mempalace_diary_write, mempalace_search

log = logging.getLogger(__name__)
_DB_FILE = os.path.join(os.path.dirname(__file__), "..", "data", "gtm_agent_sessions.db")


async def arun_with_backoff(agent, prompt: str, max_retries: int = 4):
    """Call agent.arun with exponential backoff on 429 rate limit errors."""
    if MOCK_MODE:
        return type('obj', (object,), {
            'content': json.dumps({
                "plan": ["Mock Discovery", "Mock Enrichment", "Mock Strategy"],
                "target_signals": ["Mock Hiring Signal"],
                "company_filters": {"has_website": {"value": True}},
                "prospect_filters": {},
                "reasoning": "Mock reasoning for local testing.",
                "confidence": 1.0,
                "status": "success",
                "buying_signals": ["Recently hired 5 SDRs"],
                "tech_stack": ["React", "Python"],
                "personas": [{"hook": "Saw you are hiring!", "message_angle": "Sales Optimization"}]
            })
        })()
    log.info(
        f"[groq] [{agent.name}] prompt ({len(prompt)} chars):\n"
        f"{'─' * 60}\n{prompt.strip()}\n{'─' * 60}"
    )
    for attempt in range(max_retries):
        try:
            response = await agent.arun(prompt)
            content_str = getattr(response, 'content', str(response))
            
            # Agno silently swallows HTTP 503/429 errors from Groq and prints them as valid string outputs. 
            # We must detect these swallowed API errors natively and force the retry backoff.
            if '"error"' in content_str and ('"code": 503' in content_str or '"code": 429' in content_str):
                raise ValueError(f"Agno API Swallowed Error: {content_str[:150]}")
                
            log.info(
                f"[groq] [{agent.name}] response (attempt {attempt + 1}):\n"
                f"{'─' * 60}\n{content_str}\n{'─' * 60}"
            )
            return response
        except Exception as e:
            error_str = str(e).lower()
            # Check for rate limit, service unavailable, and networking errors
            is_retryable = any(x in error_str for x in [
                "429", "503", "quota", "rate", "resource_exhausted", 
                "unavailable", "service unavailable", "high demand",
                "connection", "timeout", "read_error"
            ])
            
            if is_retryable:
                wait = 2 ** attempt  # 1s, 2s, 4s, 8s
                if any(x in error_str for x in ["429", "quota", "rate", "503"]):
                    log.warning(f"Groq API rejection hit, backoff initiated.")
                
                log.warning(f"Retrying in {wait}s (attempt {attempt+1}/{max_retries}) based on error: {error_str[:100]}")
                await asyncio.sleep(wait)
            else:
                log.error(f"[groq] [{agent.name}] non-retryable error on attempt {attempt + 1}: {e}")
                raise
    # Final attempt — let it raise, but still log the response if it succeeds
    response = await agent.arun(prompt)
    log.info(
        f"[groq] [{agent.name}] response (final attempt):\n"
        f"{'─' * 60}\n{getattr(response, 'content', str(response))}\n{'─' * 60}"
    )
    return response


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
    def __init__(self, name: str, description: str, tools: List[Any] = None, instructions: List[str] = None, use_tools: bool = True):
        self.name = name
        self.description = description
        self.use_tools = use_tools
        self.default_tools = [mempalace_diary_write, mempalace_search] if use_tools else []
        self.tools = self.default_tools + (tools or [])
        self.instructions = instructions or []

        global MOCK_MODE
        if MOCK_MODE:
            self.agent = type('obj', (object,), {'name': self.name})()
            return

        try:
            self.agent = Agent(
                name=self.name,
                description=self.description,
                model=Groq(id="llama-3.3-70b-versatile", api_key=os.getenv("GROQ_API_KEY")),
                tools=self.tools,
                instructions=self.instructions + [
                    "Always return your final answer in the requested JSON format."
                ],
                markdown=True,
                add_history_to_context=True,
                db=SqliteDb(db_file=_DB_FILE),
            )
        except Exception as e:
            log.error(f"Failed to instantiate Agent {self.name} with Groq model: {e}")
            MOCK_MODE = True
            self.agent = type('obj', (object,), {'name': self.name})()

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