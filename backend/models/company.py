from pydantic import BaseModel, Field
from typing import List, Optional, Dict

class BuyingSignal(BaseModel):
    type: str
    description: str
    score: float
    timestamp: str

class CompanyRecord(BaseModel):
    name: Optional[str] = None
    industry: Optional[str] = None
    location: Optional[str] = None
    description: Optional[str] = None
    website: Optional[str] = None
    funding_round: Optional[str] = None
    funding_amount: Optional[float] = None
    funding_date: Optional[str] = None
    employee_count: Optional[int] = None

class EnrichedRecord(CompanyRecord):
    tech_stack: List[str] = []
    hiring_signals: List[str] = []
    buying_signals: List[BuyingSignal] = []
    buying_signal_score: float = 0.0
    icp_score: float = 0.0
    reasoning: Optional[str] = None
