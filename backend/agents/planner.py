from .base import BaseGTMAgent, parse_llm_json, arun_with_backoff
from models.agents import AgentInput, AgentOutput
from .base import AgentRegistry

class PlannerAgent(BaseGTMAgent):
    def __init__(self):
        super().__init__(
            name="planner",
            description="Creates a step-by-step execution plan for the GTM intelligence run.",
            use_tools=False,
            instructions=[
                "Break down the GTM query into logical execution phases: Discovery, Signals, Validation, and Strategy.",
                "Extract structured Explorium API JSON filters for 'company_filters' and 'prospect_filters'.",
                "Valid company filters: 'country_code', 'company_size', 'company_revenue', 'company_age', 'is_public_company', 'linkedin_category', 'website_keywords', 'events'. Use {'values': ['...']} for arrays, {'value': bool} for boolean.",
                "IMPORTANT: The 'industry' field DOES NOT EXIST. You MUST use 'linkedin_category'. Only use values from the VALID_LINKEDIN_CATEGORIES list below — never invent or guess a category.",
                # === VALID LINKEDIN CATEGORIES (use exactly as written) ===
                "VALID_LINKEDIN_CATEGORIES: "
                "'information technology and services', "
                "'computer software', "
                "'internet', "
                "'financial services', "
                "'computer & network security', "
                "'software development', "
                "'telecommunications', "
                "'semiconductors', "
                "'computer hardware', "
                "'cloud computing', "
                "'data analytics', "
                "'banking', "
                "'investment banking', "
                "'venture capital & private equity', "
                "'hospital & health care', "
                "'biotechnology', "
                "'pharmaceuticals'. "
                "Only choose from this list. If none fits perfectly, pick the closest match.",
                # === CATEGORY MAPPING (common user intents -> correct LinkedIn category) ===
                "CATEGORY MAPPING: "
                "'cybersecurity' / 'cyber security' / 'infosec' -> 'computer & network security'. "
                "'saas' / 'b2b software' / 'enterprise software' -> 'computer software'. "
                "'fintech' / 'payments' -> 'financial services'. "
                "'healthtech' / 'health IT' -> 'hospital & health care'. "
                "'biotech' -> 'biotechnology'. "
                "'pharma' -> 'pharmaceuticals'. "
                "'vc' / 'private equity' / 'pe' -> 'venture capital & private equity'. "
                "'semiconductor' / 'chips' -> 'semiconductors'. "
                "'networking' / 'telecom' -> 'telecommunications'. "
                "'cloud' / 'aws' / 'azure' / 'gcp' -> 'cloud computing'. "
                "'analytics' / 'data science' / 'big data' -> 'data analytics'. "
                "Never use a category not in VALID_LINKEDIN_CATEGORIES.",
                "If using 'events', schema MUST be: {'values': ['new_funding_round'], 'last_occurrence': 90}. Never invent event names.",

                # === GENERIC FUNDING STAGE -> FILTER MAPPING ===
                # Explorium has no direct 'funding stage' filter. Map intent to size/revenue/age combos.
                "FUNDING STAGE MAPPING (apply these filters when the user mentions a funding stage):",
                "  Seed/Pre-seed   -> company_size: ['1-10','11-50'],               company_revenue: ['0-500K','500K-1M'],        company_age: ['0-3'],       is_public_company: {value: false}",
                "  Series A        -> company_size: ['11-50','51-200'],              company_revenue: ['1M-5M','5M-10M'],          company_age: ['0-3','3-6'], is_public_company: {value: false}",
                "  Series B        -> company_size: ['51-200','201-500'],            company_revenue: ['10M-25M','25M-75M'],       company_age: ['3-6','6-10'],is_public_company: {value: false}",
                "  Series C        -> company_size: ['201-500','501-1000'],          company_revenue: ['25M-75M','75M-200M'],      company_age: ['6-10'],      is_public_company: {value: false}",
                "  Late Stage/Growth -> company_size: ['501-1000','1001-5000'],      company_revenue: ['75M-200M','200M-500M'],                               is_public_company: {value: false}",
                "  Enterprise/Public -> company_size: ['1001-5000','5001-10000','10001+'], is_public_company: {value: true}",
                "  When user asks for 'recent [stage] funding', ALSO add: events: {values: ['new_funding_round'], last_occurrence: 90}",

                # === VALID ENUM REFERENCE (docs-verified) ===
                "VALID company_size: '1-10','11-50','51-200','201-500','501-1000','1001-5000','5001-10000','10001+'",
                "VALID company_revenue: '0-500K','500K-1M','1M-5M','5M-10M','10M-25M','25M-75M','75M-200M','200M-500M','500M-1B','1B-10B','10B-100B'",
                "VALID company_age: '0-3','3-6','6-10','10-20','20+'",

                # === PROSPECT FILTERS ===
                "Valid prospect filters: 'job_level' (STRICTLY FROM: 'owner','c-suite','vice president','director','manager','partner','non-managerial','junior','president','senior manager','advisor','founder','board member'), 'job_department' (STRICTLY FROM: 'administration','c-suite','engineering','strategy','product','sales','customer success','security','it','support','marketing','legal','operations','data','finance'). Use {'values': [...]}.",
                "Keep the plan concise and actionable."
            ]
        )

    async def run(self, input_data: AgentInput) -> AgentOutput:
        identity = (input_data.context or {}).get("identity", "")
        prompt = f"""
        Create a precise GTM intelligence execution plan for this query: '{input_data.query}'
        
        Additional context: {identity}

        Apply FUNDING STAGE MAPPING and VALID ENUM REFERENCE from your instructions for precise Explorium filters.

        Return ONLY a JSON object with no markdown:
        {{
          "plan": ["step 1", "step 2", ...],
          "target_signals": ["signal type 1", "signal type 2", ...],
          "company_filters": {{ "country_code": {{"values": ["us"]}}, "linkedin_category": {{"values": ["software development"]}} }},
          "prospect_filters": {{ }},
          "reasoning": "one sentence explaining the strategy",
          "confidence": 0.0-1.0
        }}
        """
        try:
            response = await arun_with_backoff(self.agent, prompt)
            parsed = parse_llm_json(response.content)
            return AgentOutput(
                agent_name=self.name,
                status="success",
                data={
                  "plan": parsed.get("plan", []),
                  "target_signals": parsed.get("target_signals", []),
                  "company_filters": parsed.get("company_filters", {"has_website": {"value": True}}),
                  "prospect_filters": parsed.get("prospect_filters", {})
                },
                confidence=parsed.get("confidence", 0.8),
                reasoning=parsed.get("reasoning", "")
            )
        except Exception as e:
            return AgentOutput(agent_name=self.name, status="error",
                               data={}, confidence=0.0, reasoning=str(e))

AgentRegistry.register(PlannerAgent())