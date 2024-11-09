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
        if self.root and self.root != target.root_id:
            return False
        if self.state and target.state and not self.state in target.state:
            return False
        if self.categories and target.categories:
            one_found = False
            # Assume that categories contains categories separated by commas
            tcats = target.categories.split(",")
            for c in self.categories:
                if c in tcats:
                    one_found = True
            if not one_found:
                return False
        return True
