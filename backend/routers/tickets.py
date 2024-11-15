from ..schemas.categories import States
from ..schemas.ticket_subscription import TicketSubscription
from ..schemas.user import User
from ..schemas.ticket import Ticket
from ..schemas.database_init import SessionDep
from ..schemas.filter import Filter
from .users import read_user_tickets
from fastapi import APIRouter, HTTPException
from sqlmodel import select
import datetime


router = APIRouter()


def apply_filter(filter: Filter, targets: list[Ticket], session: SessionDep) -> list[Ticket]:
    res: list[Ticket] = []
    uticks = []
    if (filter.user_id and filter.user_id != ""):
        uticks = read_user_tickets(filter.user_id, session)
    for target in targets:
        add = True
        if filter.id and target.id == filter.id:
            add = False
        if filter.created_after and target.created_at and filter.created_after > target.created_at:
            add = False
        if filter.created_before and target.created_at and filter.created_before < target.created_at:
            add = False
        if filter.root and target.root_id and filter.root != target.root_id:
            add = False
        if filter.status and target.status and not filter.status in States:
            add = False
        if filter.categories and target.categories and filter.categories != target.categories:
            add = False
        if not target.categories:
            add = False
        if filter.user_id and filter.user_id != "":
            a = False
            for ut in uticks:
                if ut.id == target.id:
                    a = True
            add = a

        if add:
            res.append(target)

    return res


@router.post("/api/tickets/")
def create_ticket(ticket: Ticket, session: SessionDep) -> Ticket:
    Ticket.model_validate(ticket)
    date = datetime.datetime.now()
    ticket.created_at = date.timestamp()
    ticket.updated_at = date.timestamp()
    ticket.id = datetime.datetime.now().strftime("%M%S")
    session.add(ticket)
    session.commit()
    session.refresh(ticket)
    return ticket


@router.get("/api/tickets/{ticket_id}")
def read_ticket(ticket_id: int, session: SessionDep) -> Ticket:
    ticket = session.get(Ticket, ticket_id)
    if not ticket:
        raise HTTPException(status_code=404, detail="Ticket not found")
    return ticket


@router.post("/api/tickets/all")
def read_tickets(f: Filter, session: SessionDep) -> list[Ticket]:
    tickets = session.exec(select(Ticket)).all()
    if not tickets:
        raise HTTPException(status_code=404, detail="Tickets not found")
    return apply_filter(f, list(tickets), session) # pyright: ignore


@router.post("/api/tickets/root/{root_id}")
def get_api_tickets(f: Filter, root_id: str, session: SessionDep) -> list[Ticket]:
    tickets = session.exec(select(Ticket).where(Ticket.root_id == root_id)).all()
    if not tickets:
        raise HTTPException(status_code=404, detail="Ticket not found")
    return apply_filter(f, list(tickets), session) # pyright: ignore


@router.put("api/tickets/{ticket_id}")
def update_ticket(ticket_id: int, ticket: Ticket, session: SessionDep):
    Ticket.model_validate(ticket)
    db_ticket = session.get(Ticket, ticket_id)
    if not db_ticket:
        raise HTTPException(status_code=404, detail="Ticket not found")
    update_data = ticket.dict(exclude_unset=True)
    for key, value in update_data.items():
        setattr(db_ticket, key, value)
    session.add(db_ticket)
    session.commit()
    session.refresh(db_ticket)
    return db_ticket
