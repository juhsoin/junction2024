from sqlmodel import SQLModel, Field
from typing import Optional

class TicketSubscription(SQLModel, table=True):
    id: Optional[str] = Field(default=None, primary_key=True)
    user_id: str
    ticket_id: str