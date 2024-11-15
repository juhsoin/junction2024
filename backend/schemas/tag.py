from typing import Optional
from sqlmodel import SQLModel, Field

class Ticket(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    tag_id: int
    description: str
    