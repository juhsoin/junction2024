from typing import Optional
from sqlmodel import SQLModel, Field

class Api(SQLModel, table=True):
    id: Optional[str] = Field(default=None, primary_key=True)
    title: str
    description: str
    status: str
    created_at: Optional[str] = None
    updated_at: Optional[str] = None
