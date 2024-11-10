from typing import Optional
from sqlmodel import SQLModel, Field

class Api(SQLModel, table=True):
    id: Optional[str] = Field(default=None, primary_key=True)
    title: str
    description: str
    status: str
    created_at: Optional[float] = None
    updated_at: Optional[float] = None
    update_summary: Optional[str] = None
    version: Optional[str] = None
    next_release: Optional[str] = None
