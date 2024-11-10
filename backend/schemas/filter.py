from typing import Optional
from sqlmodel import SQLModel
from .categories import States

class Filter(SQLModel):
    id: Optional[str] = None
    status: Optional[str] = None
    created_after: Optional[float] = None
    updated_after: Optional[float] = None
    created_before: Optional[float] = None
    updated_before: Optional[float] = None
    categories: Optional[str] = None
    state: Optional[States] = None
    root: Optional[str] = None
    user_id: Optional[str] = None
