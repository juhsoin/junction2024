from sqlmodel import SQLModel, Field
from typing import Optional
from datetime import datetime

class User(SQLModel, table=True):
    id: Optional[str] = Field(default=None, primary_key=True)
    organization_id: int
    username: str
    email: str
    is_active: bool = Field(default=True)
