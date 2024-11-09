from sqlmodel import SQLModel, Field
from typing import Optional
import datetime

class TicketSubscription(SQLModel, table=True):
    id: Optional[str] = Field(default=None, primary_key=True)
    user_id: str = Field(default=None, foreign_key="user.id")
    ticket_id: str = Field(default=None, foreign_key="ticket.id")
