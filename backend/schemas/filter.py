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

    def apply(self, target) -> bool:
        if self.id and target.id != self.id:
            return False
        if self.created_after and target.created_at and self.created_after > target.created_at:
            return False
        if self.created_before and target.created_at and self.created_before < target.created_at:
            return False
        if self.root and target.root and self.root != target.root_id:
            return False
        if self.state and target.state and not self.state in target.state:
            return False
        if self.categories and target.categories != None and self.categories != target.categories:
            return False
        return True
