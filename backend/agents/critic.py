from .base import BaseGTMAgent, parse_llm_json, arun_with_backoff
from models.agents import AgentInput, AgentOutput
from .base import AgentRegistry
import json

class CriticAgent(BaseGTMAgent):
    def __init__(self):
        super().__init__(
            name="critic",
            description="Validates the factual accuracy of generated outreach hooks against raw signal data.",
            use_tools=False,
            instructions=[
                "You are a Hallucination & Contradiction Detector, NOT a query-intent checker.",
                "Your ONLY job is to detect fabrications or contradictions in the generated persona hooks, email snippets, and competitive intel.",
                "REJECT ONLY IF: (1) A hook mentions a technology the company does NOT use (e.g., says 'AWS' but tech stack shows 'GCP'). (2) A hook contradicts a direct data signal (e.g., talks about 'rapid expansion' but signals show 'cost_cutting' event). (3) A hook invents specific named products, acquisitions, or events not present in the data.",
                "DO NOT REJECT for: missing funding data, low buying_signal_score, mismatch with query intent, or because the company seems like a wrong fit. These are data availability issues, not hallucinations.",
                "If no signals exist (empty hiring_signals, no funding, no strategic_events), the hooks MUST be appropriately cautious (consultative/neutral). REJECT if they are aggressively event-driven despite no signals.",
                "PASS if the hooks are grounded in the available data or appropriately hedged given data gaps.",
            ]
        )

    async def run(self, input_data: AgentInput) -> AgentOutput:
        companies = input_data.context.get("companies", [])
        prompt = f"""
        You are a Hallucination & Contradiction Detector for GTM outreach hooks.

        Companies (Raw Signals + Generated Hooks):
        {json.dumps(companies, indent=2)}

        Evaluate ONLY:
        1. HALLUCINATIONS: Does any hook mention a technology, tool, or product NOT present in tech_stack?
        2. SIGNAL CONTRADICTIONS: Does any hook assert active growth/expansion when the signals show cost_cutting, layoffs, or decrease_in_* events?
        3. OVERCONFIDENCE ON EMPTY DATA: If hiring_signals=[], funding=null, strategic_events=[], do the hooks fabricate specific triggers (e.g., "after your recent Series B" when funding is null)?

        DO NOT reject because the company doesn't match the user's query intent. That is not your scope.

        Return ONLY a JSON object:
        {{
          "verdict": "PASS" or "REJECT",
          "issues": ["issue 1", "issue 2"],
          "reasoning": "one sentence explaining the verdict",
          "confidence": 0.0-1.0
        }}

        REJECT only for genuine fabrications or direct signal contradictions.
        """
        try:
            response = await arun_with_backoff(self.agent, prompt)
            parsed = parse_llm_json(response.content)
            return AgentOutput(
                agent_name=self.name,
                status=parsed.get("verdict", "PASS"),
                data={"issues": parsed.get("issues", [])},
                confidence=parsed.get("confidence", 0.9),
                reasoning=parsed.get("reasoning", "")
            )
        except Exception as e:
            return AgentOutput(agent_name=self.name, status="PASS",
                               data={}, confidence=0.5, reasoning=str(e))

AgentRegistry.register(CriticAgent())