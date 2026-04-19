from .base import BaseGTMAgent, parse_llm_json, arun_with_backoff
from models.agents import AgentInput, AgentOutput
from .base import AgentRegistry
import asyncio, logging

log = logging.getLogger(__name__)

class ToolSelectionAgent(BaseGTMAgent):
    def __init__(self):
        super().__init__(
            name="tool_selection",
            description="Selects the appropriate tools and data sources for the GTM task.",
            use_tools=False,
            instructions=[
                "Analyze the user query to determine which GTM tools are needed.",
                "Available tools include: search_companies, get_hiring_signals, get_funding_info, get_tech_stack, get_leadership_changes, enrich_company.",
                "Provide a rationale for why each tool was selected."
            ]
        )

    async def run(self, input_data: AgentInput) -> AgentOutput:
        prompt = f"""
        Given this GTM query: '{input_data.query}'
        Available tools: search_companies, get_hiring_signals, get_tech_stack,
                         get_funding_info, get_leadership_changes, enrich_company

        Reason about which signals are most relevant to this specific query.
        Return ONLY a JSON object:
        {{
          "selected_tools": ["tool_name_1", "tool_name_2"],
          "priority_signals": ["signal type 1", "signal type 2"],
          "reasoning": "why these tools match the query intent",
          "confidence": 0.0-1.0
        }}
        """
        try:
            response = await arun_with_backoff(self.agent, prompt)
            parsed = parse_llm_json(response.content)
            # log
            log.info(f"[tool_selection] selected tools: {parsed.get('selected_tools', [])} with confidence {parsed.get('confidence', 0.0)}")
            return AgentOutput(
                agent_name=self.name, status="success",
                data={"selected_tools": parsed.get("selected_tools", []),
                      "priority_signals": parsed.get("priority_signals", [])},
                confidence=parsed.get("confidence", 0.9),
                reasoning=parsed.get("reasoning", "")
            )
        except Exception as e:
            return AgentOutput(agent_name=self.name, status="error",
                               data={}, confidence=0.0, reasoning=str(e))

AgentRegistry.register(ToolSelectionAgent())