from typing import Optional
from sqlmodel import SQLModel, Field
from .categories import States

class Ticket(SQLModel, table=True):
    id: Optional[str] = Field(default=None, primary_key=True)
    title: str
    description: str
    status: States
    created_at: Optional[float] = None
    updated_at: Optional[float] = None
    root_id: Optional[str] = Field(default=None, foreign_key="api.id")
    development_proposal_and_clarification: Optional[str] = None
    ball_park_estimate: Optional[str]
    impact_on_market: Optional[int] = Field(default=None, ge=0, le=3)
    priority: Optional[int] = Field(default=None, ge=1, le=3)
    argumentation_for_proposal: Optional[str]
    proposal_impact: Optional[str]
    next_steps: Optional[str]
    categories: Optional[str]
    planned_release_version: Optional[str]
