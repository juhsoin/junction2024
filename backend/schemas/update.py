from typing import Optional
from sqlmodel import SQLModel, Field

class Update(SQLModel, table=True):
    id: Optional[str] = Field(default=None, primary_key=True)
    title: str
    description: str
    status: str
    created_at: Optional[float] = None
    updated_at: Optional[float] = None
    root_id: str # ticket id
    development_proposal_and_clarification: Optional[str] = None
    ball_park_estimate: Optional[str]
    impact_on_market: Optional[int] = Field(default=None, ge=0, le=3)
    priority: Optional[int] = Field(default=None, ge=1, le=3)
    argumentation_for_proposal: Optional[str]
    proposal_impact: Optional[str]
    next_steps: Optional[str]
    workgroup: Optional[str]
    othernotes: Optional[str]
    categories: Optional[str]
