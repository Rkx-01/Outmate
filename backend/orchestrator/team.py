import uuid
import asyncio
import json
import os
import time
from datetime import datetime
from typing import List, Dict, Any, AsyncGenerator
from agents.base import AgentRegistry
from models.agents import AgentInput, AgentOutput
from models.events import SSEEvent
from memory.traditional import TraditionalCache
from memory.mempalace import MemPalaceClient

class GTMTeamOrchestrator:
    def __init__(self, cache: TraditionalCache):
        self.cache = cache
        self.mempalace = MemPalaceClient()
        self.max_retries = 1

    def _log_run(self, event_type: str, data: Any):
        log_entry = {
            "timestamp": uuid.uuid4().hex,
            "event_type": event_type,
            "data": data
        }
        os.makedirs("logs", exist_ok=True)
        with open("logs/agent_runs.jsonl", "a") as f:
            f.write(json.dumps(log_entry) + "\n")

    async def run_pipeline(self, query: str, session_id: str = None) -> AsyncGenerator[SSEEvent, None]:
        session_id = session_id or str(uuid.uuid4())
        retry_count = 0
        current_companies = []
        reasoning_trace = []
        final_plan_data = {}
        pipeline_start = time.time()
        
        # 0. Wake up MemPalace
        identity = self.mempalace.get_wake_up_context()
        
        # Emit pipeline_start
        yield SSEEvent(event_type="pipeline_start", data={
            "run_id": session_id,
            "query": query,
            "timestamp": datetime.utcnow().isoformat(),
            "total_agents": 6
        })

        # 1. Tool Selection
        yield self._step_start("tool_selection", 1)
        step_start = time.time()
        tool_agent = AgentRegistry.get_agent("tool_selection")
        tool_result = await tool_agent.run(AgentInput(query=query))
        reasoning_trace.append(tool_result.reasoning)
        yield self._step_done("tool_selection", tool_result.confidence, round((time.time() - step_start) * 1000))

        while retry_count <= self.max_retries:
            try:
                # 2. Planner
                yield self._step_start("planner", retry_count + 1)
                step_start = time.time()
                planner = AgentRegistry.get_agent("planner")
                plan_result = await planner.run(AgentInput(
                    query=query,
                    context={"identity": identity}
                ))
                final_plan_data = plan_result.data.get("plan", {})
                reasoning_trace.append(plan_result.reasoning)
                yield self._step_done("planner", plan_result.confidence, round((time.time() - step_start) * 1000))

                # 3. Retrieval
                yield self._step_start("retrieval", retry_count + 1)
                step_start = time.time()
                retrieval = AgentRegistry.get_agent("retrieval")
                ret_result = await retrieval.run(AgentInput(
                    query=query, 
                    context={
                        "company_filters": plan_result.data.get("company_filters", {}),
                        "prospect_filters": plan_result.data.get("prospect_filters", {})
                    }
                ))
                current_companies = ret_result.data
                reasoning_trace.append(ret_result.reasoning)
                self._log_run("retrieval_result", {
                    "company_count": len(current_companies),
                    "companies": [{"name": c.get("name"), "explorium_id": c.get("explorium_id")} for c in current_companies],
                    "reasoning": ret_result.reasoning,
                    "status": ret_result.status,
                })
                yield self._step_done("retrieval", ret_result.confidence, round((time.time() - step_start) * 1000))

                # 4. Autonomous Routing: Enrichment
                # To minimize Gemini costs, we dynamically check if Retrieval already pulled perfect data.
                companies_needing_enrichment = [c for c in current_companies if not c.get("buying_signals") or not c.get("tech_stack")]
                companies_skipping_enrichment = [c for c in current_companies if c not in companies_needing_enrichment]

                if companies_needing_enrichment:
                    yield self._step_start("enrichment", retry_count + 1)
                    step_start = time.time()
                    enrichment = AgentRegistry.get_agent("enrichment")
                    enr_result = await enrichment.run(AgentInput(query=query, context={"companies": companies_needing_enrichment}))
                    
                    # Merge back the autonomous bypass stream with the enriched stream
                    enriched_data = enr_result.data if enr_result.data else []
                    current_companies = companies_skipping_enrichment + enriched_data
                    
                    if hasattr(enr_result, 'reasoning') and enr_result.reasoning:
                        reasoning_trace.append(enr_result.reasoning)
                        
                    self._log_run("enrichment_result", {
                        "company_count": len(current_companies),
                        "companies_skipped": len(companies_skipping_enrichment),
                        "status": enr_result.status,
                    })

                    partial_event = SSEEvent(event_type="partial_result", data={"companies": current_companies})
                    self._log_run(partial_event.event_type, partial_event.data)
                    yield partial_event
                    
                    yield self._step_done("enrichment", enr_result.confidence, round((time.time() - step_start) * 1000))
                else:
                    # Autonomous Bypass -> No Gemini Token Burn!
                    reasoning_trace.append("Orchestrator bypassed Enrichment dynamically. All targeted companies met deterministic threshold standards.")
                    yield self._step_start("enrichment", retry_count + 1)
                    yield self._step_done("enrichment", 1.0, 0)
                    # Provide a stub so enr_result is always defined for confidence calc below
                    enr_result = AgentOutput(agent_name="enrichment", status="bypass", data=[], confidence=1.0, reasoning="bypassed")


                # 5. GTM Strategy
                yield self._step_start("gtm_strategy", retry_count + 1)
                step_start = time.time()
                strategy_agent = AgentRegistry.get_agent("gtm_strategy")
                strat_result = await strategy_agent.run(AgentInput(query=query, context={"companies": current_companies}))
                current_companies_with_strats = strat_result.data
                reasoning_trace.append(strat_result.reasoning)
                self._log_run("gtm_strategy_result", {
                    "company_count": len(strat_result.data) if strat_result.data else 0,
                    "companies": [{"name": c.get("name"), "has_personas": bool(c.get("personas"))} for c in (strat_result.data or [])],
                    "reasoning": strat_result.reasoning,
                    "status": strat_result.status,
                })
                yield self._step_done("gtm_strategy", strat_result.confidence, round((time.time() - step_start) * 1000))

                # 6. Critic
                yield self._step_start("critic", retry_count + 1)
                step_start = time.time()
                critic = AgentRegistry.get_agent("critic")
                critic_result = await critic.run(AgentInput(query=query, context={"companies": current_companies_with_strats}))
                reasoning_trace.append(critic_result.reasoning)
                
                if critic_result.status == "REJECT":
                    retry_count += 1
                    reject_event = SSEEvent(event_type="agent_done", data={
                        "agent": "critic",
                        "verdict": "REJECT",
                        "reason": critic_result.reasoning,
                        "duration_ms": round((time.time() - step_start) * 1000)
                    })
                    self._log_run(reject_event.event_type, reject_event.data)
                    yield reject_event

                    if retry_count > self.max_retries:
                        # Max retries exhausted — accept best-effort output with a warning flag
                        # instead of looping forever or erroring out.
                        retry_limit_event = SSEEvent(event_type="agent_retry", data={
                            "agent": "pipeline",
                            "attempt": retry_count,
                            "reason": "Max critic retries reached. Accepting best-effort results with quality warning."
                        })
                        self._log_run(retry_limit_event.event_type, retry_limit_event.data)
                        yield retry_limit_event
                        # Tag companies with a data quality warning so the frontend can surface it
                        for c in current_companies_with_strats:
                            c["data_quality_warning"] = critic_result.reasoning
                        break  # Exit the retry loop and proceed to final output

                    retry_event = SSEEvent(event_type="agent_retry", data={"agent": "planner", "attempt": retry_count + 1, "reason": critic_result.reasoning})
                    self._log_run(retry_event.event_type, retry_event.data)
                    yield retry_event
                    continue
                
                pass_event = SSEEvent(event_type="agent_done", data={
                    "agent": "critic", 
                    "verdict": "PASS",
                    "duration_ms": round((time.time() - step_start) * 1000)
                })
                self._log_run(pass_event.event_type, pass_event.data)
                yield pass_event

                # Final Output Aggregation
                results = []
                all_signals = []
                all_hooks = []
                all_angles = []
                all_snippets = []
                
                for c in current_companies_with_strats:
                    # Hoist key fields from deep_enrichment to top-level before stripping
                    # This ensures employee_count, headquarters, description etc. are always populated.
                    deep = c.get("deep_enrichment") or {}
                    if not c.get("employee_count") and deep.get("number_of_employees_range"):
                        c["employee_count"] = deep["number_of_employees_range"]
                    if not c.get("headquarters") and deep.get("city_name"):
                        city = deep.get("city_name", "").title()
                        region = deep.get("region", "").title()
                        c["headquarters"] = f"{city}, {region}".strip(", ") if city or region else None
                    if not c.get("description") and deep.get("business_description"):
                        c["description"] = deep["business_description"]
                    if not c.get("industry") and deep.get("naics_description"):
                        c["industry"] = deep["naics_description"]
                    if not c.get("logo") and deep.get("logo"):
                        c["logo"] = deep["logo"]
                    if not c.get("linkedin_profile") and deep.get("linkedin_profile"):
                        c["linkedin_profile"] = deep["linkedin_profile"]
                    if not c.get("revenue_range") and deep.get("yearly_revenue_range"):
                        c["revenue_range"] = deep["yearly_revenue_range"]
                    # Fix website URL: ensure https:// prefix
                    if c.get("website") and not c["website"].startswith("http"):
                        c["website"] = "https://" + c["website"]

                    # Strip heavy/redundant signal keys from the clean results array
                    exclude_keys = ["hiring_signals", "tech_stack", "funding", "deep_enrichment", "leadership_changes", "strategic_events", "buying_signals", "reasoning", "prospects"]
                    result_c = {k: v for k, v in c.items() if k not in exclude_keys}
                    results.append(result_c)
                    
                    # Accumulate global signals
                    company_name = c.get("name", "Unknown")
                    if "hiring_signals" in c and c["hiring_signals"]:
                        all_signals.extend([{"type": "hiring", "description": s, "company": company_name} for s in c["hiring_signals"]])
                    if "funding" in c and c["funding"]:
                        all_signals.append({"type": "funding", "description": f"{c['funding'].get('funding_round', '')} - {c['funding'].get('funding_amount', '')}", "company": company_name})
                    
                    # Accumulate global strategy
                    for p in c.get("personas", []):
                        if p.get("hook"): all_hooks.append(p.get("hook"))
                        if p.get("message_angle"): all_angles.append(p.get("message_angle"))
                        if p.get("email_snippet"): all_snippets.append(p.get("email_snippet"))
                    if "competitive_intel" in c:
                        if c["competitive_intel"].get("displacement_angle"):
                            all_angles.append(c["competitive_intel"]["displacement_angle"])

                final_output = {
                    "session_id": session_id,
                    "query": query,
                    "plan": final_plan_data,
                    "results": results,
                    "signals": all_signals,
                    "gtm_strategy": {
                        "hooks": all_hooks,
                        "angles": all_angles,
                        "email_snippets": all_snippets
                    },
                    "confidence": (ret_result.confidence + enr_result.confidence + strat_result.confidence) / 3,
                    "reasoning_trace": reasoning_trace
                }
                
                self.cache.save_run(session_id, query, final_output["confidence"], len(current_companies), retry_count, False, final_output)
                
                final_event = SSEEvent(event_type="final_output", data=final_output)
                self._log_run(final_event.event_type, final_event.data)
                yield final_event

                # Emit pipeline_complete
                yield SSEEvent(event_type="pipeline_complete", data={
                    "run_id": session_id,
                    "duration_ms": round((time.time() - pipeline_start) * 1000),
                    "companies_found": len(current_companies)
                })
                return

            except Exception as e:
                error_event = SSEEvent(event_type="error", data={"message": str(e)})
                self._log_run(error_event.event_type, error_event.data)
                yield error_event
                return

        fallback_event = SSEEvent(event_type="error", data={"message": "System exhausted retries. Returning best-effort results."})
        self._log_run(fallback_event.event_type, fallback_event.data)
        yield fallback_event

    def _step_start(self, agent_name: str, attempt: int) -> SSEEvent:
        event = SSEEvent(event_type="agent_start", data={
            "agent": agent_name,
            "attempt": attempt,
            "timestamp": datetime.utcnow().isoformat()
        })
        self._log_run(event.event_type, event.data)
        return event

    def _step_done(self, agent_name: str, confidence: float, duration_ms: float) -> SSEEvent:
        event = SSEEvent(event_type="agent_done", data={
            "agent": agent_name,
            "confidence": confidence,
            "duration_ms": duration_ms
        })
        self._log_run(event.event_type, event.data)
        return event