from typing import Optional
from sqlmodel import SQLModel

class Filter(SQLModel):
    id: Optional[str] = None
    status: Optional[str] = None
    created_after: Optional[float] = None
    updated_after: Optional[float] = None
    created_before: Optional[float] = None
    updated_before: Optional[float] = None
    categories: Optional[list[str]] = None
    root: Optional[str] = None

    def apply(self, target) -> bool:
        if self.id and target.id != self.id:
            return False
        if self.created_after and target.created_at and self.created_after > target.created_at:
            return False
        if self.created_before and target.created_at and self.created_before < target.created_at:
            return False
        if self.root and self.root != target.root_id:
            return False
        return True
