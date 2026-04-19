from .base import BaseGTMAgent, parse_llm_json, arun_with_backoff
from models.agents import AgentInput, AgentOutput
from tools import (
    get_hiring_signals, get_funding_info, get_tech_stack,
    get_leadership_changes, enrich_company, get_strategic_events,
    match_business,
)
from .base import AgentRegistry
import asyncio, json, logging

log = logging.getLogger(__name__)

class EnrichmentAgent(BaseGTMAgent):
    def __init__(self):
        super().__init__(
            name="enrichment",
            description="Enriches company records with detailed signals.",
            tools=[],  # no LLM tool calls — all fetching is deterministic
            instructions=[
                "Score each company's GTM buying intent based on the signals provided.",
                "Calculate a buying_signal_score (0.0 to 1.0) and an icp_score.",
                "Return structured buying signals with type, description, score, and timestamp.",
            ]
        )

    async def fetch_signals(self, company: dict) -> dict:
        """Fetch all signals for one company deterministically."""
        name = company.get("name", "Unknown")
        website = company.get("website")
        loop = asyncio.get_event_loop()

        business_id = company.get("explorium_id")
        if not business_id:
            business_id = await loop.run_in_executor(None, match_business, name, website)
            log.info(f"[enrichment] resolved {name} -> {business_id}")

        ALL_API_EVENTS = [
            "hiring_in_sales_department", "hiring_in_engineering_department",
            "hiring_in_marketing_department", "hiring_in_operations_department",
            "hiring_in_human_resources_department", "increase_in_sales_department",
            "increase_in_engineering_department", "new_funding_round",
            "new_investment", "ipo_announcement", "employee_joined_company",
            "merger_and_acquisitions", "new_product", "new_partnership",
            "cost_cutting"
        ]

        from tools.company_api import get_business_events

        events_list, tech, deep = await asyncio.gather(
            loop.run_in_executor(None, get_business_events, business_id, ALL_API_EVENTS),
            loop.run_in_executor(None, get_tech_stack, name),
            loop.run_in_executor(None, enrich_company, business_id)
        )

        hiring = get_hiring_signals(events_list)
        funding = get_funding_info(events_list)
        leadership = get_leadership_changes(events_list)
        strategic = get_strategic_events(events_list)

        return {
            **company,
            "explorium_id": business_id,
            "tech_stack": tech or [],
            "hiring_signals": hiring or [],
            "leadership_changes": leadership or [],
            "strategic_events": strategic or [],
            "funding": funding,
            "deep_enrichment": deep,
        }

    async def run(self, input_data: AgentInput) -> AgentOutput:
        companies = input_data.context.get("companies", [])

        # Step 1: fetch all signals in parallel across all companies
        enriched = await asyncio.gather(*(self.fetch_signals(c) for c in companies))
        enriched = list(enriched)
        log.info(f"[enrichment] signals fetched for {len(enriched)} companies")

        # Step 2: ONE single LLM call to score all companies at once
        prompt = f"""
        Score each company's GTM buying intent based on their signals.

        Companies with signals:
        {json.dumps([{
            "name": c.get("name"),
            "hiring_signals": c.get("hiring_signals"),
            "tech_stack": c.get("tech_stack"),
            "funding": c.get("funding"),
            "leadership_changes": c.get("leadership_changes"),
            "strategic_events": c.get("strategic_events"),
        } for c in enriched], indent=2)}

        Return ONLY a JSON array, one object per company in the same order:
        [
          {{
            "name": str,
            "buying_signal_score": 0.0-1.0,
            "icp_score": 0.0-1.0,
            "buying_signals": [
              {{"type": str, "description": str, "score": 0.0-1.0, "timestamp": str}}
            ],
            "reasoning": "one sentence"
          }}
        ]
        """
        try:
            response = await arun_with_backoff(self.agent, prompt)
            scores = parse_llm_json(response.content)
            if not isinstance(scores, list):
                scores = []
        except Exception as e:
            log.warning(f"[enrichment] LLM scoring failed: {e}, using defaults")
            scores = []

        # Merge scores back by position
        score_map = {s.get("name"): s for s in scores}
        for c in enriched:
            s = score_map.get(c.get("name"), {})
            c["buying_signal_score"] = s.get("buying_signal_score", 0.5)
            c["icp_score"] = s.get("icp_score", 0.5)
            c["buying_signals"] = s.get("buying_signals", [])
            c["reasoning"] = s.get("reasoning", "")

        return AgentOutput(
            agent_name=self.name, status="success",
            data=enriched, confidence=0.8,
            reasoning=f"Enriched {len(enriched)} companies with Explorium signals and LLM scoring."
        )

AgentRegistry.register(EnrichmentAgent())