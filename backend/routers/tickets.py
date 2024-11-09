
from backend.schemas.ticket import Ticket
from backend.schemas.database_init import  SessionDep
from fastapi import APIRouter, HTTPException
from sqlmodel import select


router = APIRouter()


@router.post("/api/tickets/")
def create_ticket(ticket: Ticket, session: SessionDep) -> Ticket:
    Ticket.model_validate(ticket)
    session.add(ticket)
    session.commit()
    session.refresh(ticket)
    print(ticket)
    return ticket


@router.get("/api/tickets/{ticket_id}")
def read_ticket(ticket_id: int, session: SessionDep) -> Ticket:
    ticket = session.get(Ticket, ticket_id)
    if not ticket:
        raise HTTPException(status_code=404, detail="Ticket not found")
    return ticket


@router.get("/api/tickets/")
def read_tickets(session: SessionDep) -> list[Ticket]:
    tickets = session.exec(select(Ticket)).all()
    if not tickets:
        raise HTTPException(status_code=404, detail="Tickets not found")
    for t in tickets:
        print(t)
    return list(tickets)


@router.get("/api/tickets/root/{root_id}")
def get_api_tickets(root_id: int, session: SessionDep) -> list[Ticket]:
    tickets = session.exec(select(Ticket).where(Ticket.api_id == root_id))
    if not tickets:
        raise HTTPException(status_code=404, detail="Ticket not found")
    for t in tickets:
        print(t)
    return list(tickets)


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
