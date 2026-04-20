from .base import BaseGTMAgent, parse_llm_json, arun_with_backoff
from models.agents import AgentInput, AgentOutput
from .base import AgentRegistry
from config import VALID_LINKEDIN_CATEGORIES
import json, logging

log = logging.getLogger(__name__)

class GTMStrategyAgent(BaseGTMAgent):
    def __init__(self):
        categories_list = ", ".join([f"'{cat}'" for cat in VALID_LINKEDIN_CATEGORIES])
        
        super().__init__(
            name="gtm_strategy",
            description="Generates personalized GTM strategies and outreach content.",
            instructions=[
                "Create unique value propositions for CEO, VP Sales, and CTO personas.",
                "Reference specific company signals like recent funding or tech stack in the hooks.",
                "Generate full email snippets ready to be copied.",
                "Generate competitive intelligence including displacement angles and landmine questions.",
                f"Valid LinkedIn categories for industry context: {categories_list}",
                "Use industry context from company.linkedin_category (if available) to tailor messaging.",
                "You MUST return a strategy object for EVERY company provided — do not skip any.",
            ]
        )

    async def run(self, input_data: AgentInput) -> AgentOutput:
        companies = input_data.context.get("companies", [])
        prompt = f"""
        Generate GTM outreach strategies for EVERY company listed below. Do not skip any.
        Query: '{input_data.query}'
        Companies ({len(companies)} total — return exactly {len(companies)} objects):
        {json.dumps(companies, indent=2)}

        For each company produce persona-specific hooks. Return ONLY a JSON object:
        {{
          "companies": [
            {{
              ...all original company fields preserved...,
              "personas": [
                {{
                  "title": "VP Sales",
                  "pain_point": str,
                  "hook": str,
                  "message_angle": str,
                  "email_snippet": str
                }}
              ],
              "recommended_sequence": ["step 1", "step 2", "step 3"],
              "competitive_intel": {{
                "competitors": [str],
                "displacement_angle": str,
                "landmine_questions": [str]
              }}
            }}
          ],
          "reasoning": str,
          "confidence": 0.0-1.0
        }}
        """
        try:
            response = await arun_with_backoff(self.agent, prompt)
            parsed = parse_llm_json(response.content)
            returned = parsed.get("companies", [])

            # Bug 5 fix: merge strategy fields onto originals by name so dropped companies
            # are never lost — they just won't have personas/intel (shown as loading in UI)
            strategy_map = {c.get("name"): c for c in returned}
            merged = []
            for original in companies:
                name = original.get("name")
                strategy = strategy_map.get(name, {})
                merged.append({
                    **original,
                    **{k: v for k, v in strategy.items() if k in ("personas", "recommended_sequence", "competitive_intel")},
                })

            dropped = len(companies) - len(returned)
            if dropped > 0:
                log.warning(f"[gtm_strategy] Gemini dropped {dropped} companies — merged back from originals")

            return AgentOutput(
                agent_name=self.name, status="success",
                data=merged,
                confidence=parsed.get("confidence", 0.85),
                reasoning=parsed.get("reasoning", "")
            )
        except Exception as e:
            return AgentOutput(agent_name=self.name, status="error",
                               data=companies, confidence=0.0, reasoning=str(e))

AgentRegistry.register(GTMStrategyAgent())