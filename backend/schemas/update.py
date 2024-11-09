from typing import Optional
from sqlmodel import SQLModel, Field

class Update(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    title: str
    description: str
    u_type: str
    created_at: Optional[str] = None
    updated_at: Optional[str] = None
    root_id: str # ticket id
