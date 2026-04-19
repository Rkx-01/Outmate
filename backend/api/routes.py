from fastapi import APIRouter, Request, HTTPException, Depends, Header
from sse_starlette import EventSourceResponse
from pydantic import BaseModel
from typing import Optional, List
import json
import os
from .stream import sse_generator
from orchestrator.team import GTMTeamOrchestrator
from memory.traditional import TraditionalCache
from agents.base import AgentRegistry
from slowapi import Limiter
from slowapi.util import get_remote_address

router = APIRouter()
limiter = Limiter(key_func=get_remote_address)
cache = TraditionalCache()
orchestrator = GTMTeamOrchestrator(cache)

async def verify_api_key(x_api_key: str = Header(None)):
    expected_key = os.getenv("GTM_API_KEY", "dev-key")
    if x_api_key != expected_key:
        raise HTTPException(status_code=403, detail="Invalid API Key")

class RunRequest(BaseModel):
    query: str
    session_id: Optional[str] = None

@router.post("/run")
@limiter.limit("3/minute")
async def run_gtm(request: Request, run_req: RunRequest, _ = Depends(verify_api_key)):
    return EventSourceResponse(
        sse_generator(orchestrator.run_pipeline(run_req.query, run_req.session_id))
    )

@router.get("/history", dependencies=[Depends(verify_api_key)])
async def get_history():
    return {"runs": cache.get_history()}

@router.get("/history/{run_id}", dependencies=[Depends(verify_api_key)])
async def get_run_details(run_id: str):
    run_data = cache.get_run(run_id)
    if not run_data:
        raise HTTPException(status_code=404, detail="Run not found")
    return run_data

@router.get("/logs", dependencies=[Depends(verify_api_key)])
async def get_logs(run_id: Optional[str] = None):
    logs = []
    if os.path.exists("logs/agent_runs.jsonl"):
        with open("logs/agent_runs.jsonl", "r") as f:
            for line in f:
                logs.append(json.loads(line))
    return {"logs": logs}

@router.get("/health")
async def health():
    return {
        "status": "healthy",
        "mempalace": "connected",
        "agents": {a.name: {"status": "ready"} for a in AgentRegistry.list_agents()}
    }

@router.get("/agents", dependencies=[Depends(verify_api_key)])
async def list_agents():
    return {
        "agents": [
            {
                "name": a.name,
                "description": a.description,
                "tools": [t.__name__ for t in a.tools]
            }
            for a in AgentRegistry.list_agents()
        ]
    }
