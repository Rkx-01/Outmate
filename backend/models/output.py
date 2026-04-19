from pydantic import BaseModel
from typing import List, Dict, Any
from .company import EnrichedRecord

class PersonaStrategy(BaseModel):
    persona: str
    hook: str
    email_draft: str

class CompetitiveIntel(BaseModel):
    competitors: List[str]
    displacement_angle: str
    landmine_questions: List[str]

class FinalCompanyOutput(EnrichedRecord):
    strategies: List[PersonaStrategy]
    competitive_intel: CompetitiveIntel

class FinalOutput(BaseModel):
    session_id: str
    query: str
    companies: List[FinalCompanyOutput]
    overall_confidence: float
    reasoning_trace: List[str]
