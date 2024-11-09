from typing import Optional
from sqlmodel import SQLModel, Field

class Comment(SQLModel, table=True):
    id: Optional[str] = Field(default=None, primary_key=True)
    title: str
    comment: str
    user_id: str = Field(default=None, foreign_key="user.id")
    created_at: Optional[float] = None
    updated_at: Optional[float] = None
    root_id: str = Field(default=None, foreign_key="ticket.id")
