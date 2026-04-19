import asyncio, logging, json
from .base import BaseGTMAgent, parse_llm_json, arun_with_backoff, AgentRegistry
from models.agents import AgentInput, AgentOutput
from tools import search_companies, match_business, fetch_prospects

log = logging.getLogger(__name__)

class RetrievalAgent(BaseGTMAgent):
    def __init__(self):
        super().__init__(
            name="retrieval",
            description="Retrieves companies + prospects using strictly provided filters from the Planner.",
            tools=[],  # all execution here is deterministic
            instructions=[]
        )

    async def run(self, input_data: AgentInput) -> AgentOutput:
        loop = asyncio.get_event_loop()
        
        company_filters = input_data.context.get("company_filters", {"has_website": {"value": True}})
        prospect_filters = input_data.context.get("prospect_filters", {})
        
        log.info(f"[retrieval] Using filters: Companies={company_filters}, Prospects={prospect_filters}")

        # Fetch companies
        companies = await loop.run_in_executor(None, search_companies, "", company_filters)
        companies = list(companies or [])
        
        # Resolve explorium_id
        async def resolve_id(company):
            if not company.get("explorium_id"):
                bid = await loop.run_in_executor(
                    None, match_business, company.get("name"), company.get("website")
                )
                company["explorium_id"] = bid
            return company

        companies = list(await asyncio.gather(*(resolve_id(c) for c in companies)))
        companies = [c for c in companies if c.get("explorium_id")]
        
        # Fetch prospects if requested
        if prospect_filters and companies:
            job_levels = prospect_filters.get("job_level", {}).get("values")
            job_departments = prospect_filters.get("job_department", {}).get("values")
            
            async def fetch_pros(company):
                prospects = await loop.run_in_executor(
                    None, fetch_prospects, company["explorium_id"], job_levels, job_departments
                )
                company["prospects"] = prospects or []
                return company
            
            companies = list(await asyncio.gather(*(fetch_pros(c) for c in companies)))

        return AgentOutput(
            agent_name=self.name,
            status="success",
            data=companies,
            confidence=0.85,
            reasoning=f"Retrieved {len(companies)} companies. Prospect filters applied: {bool(prospect_filters)}"
        )

AgentRegistry.register(RetrievalAgent())