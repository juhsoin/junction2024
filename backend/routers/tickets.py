from ..schemas.ticket import SQLTicket, Ticket
from ..schemas.database_init import SessionDep
from ..schemas.filter import Filter
from fastapi import APIRouter, HTTPException
from sqlmodel import select
import datetime


router = APIRouter()

def transform_to_sql(ticket: Ticket) -> SQLTicket:
    sqlticket: SQLTicket = ticket.model_copy() # pyright: ignore
    sqlticket.categories = ""
    sqlticket.status = 0
    print(sqlticket)
    if ticket.categories:
        cats = []
        for c in ticket.categories:
            cats.append(c.value)
        sqlticket.categories = "" + ",".join(map(str, cats))
    if ticket.status:
        sqlticket.status = ticket.status.value
    return sqlticket

def transform_to_ticket(sqlticket: SQLTicket) -> Ticket:
    ticket: Ticket = SQLticket.__deepcopy__() # pyright: ignore
    if sqlticket.categories and len(sqlticket.categories) > 0:
        ticket.categories = sqlticket.categories.split(",") # pyright: ignore
    return ticket


@router.post("/api/tickets/")
def create_ticket(ticket: Ticket, session: SessionDep) -> Ticket:
    Ticket.model_validate(ticket)
    date = datetime.datetime.now()
    ticket.created_at = date.timestamp()
    ticket.updated_at = date.timestamp()
    ticket.id = datetime.datetime.now().strftime("%M%S")
    sqlticket = transform_to_sql(ticket)
    print("helvetti")
    print(sqlticket)
    print("tiketti")
    print(ticket)
    SQLTicket.model_validate(sqlticket)
    print("validi")
    session.add(sqlticket)
    print("sntaeohusn")
    session.commit()
    print("vittuperes")
    session.refresh(sqlticket)
    print("hlevetin kuustoista")
    return ticket


@router.get("/api/tickets/{ticket_id}")
def read_ticket(ticket_id: int, session: SessionDep) -> Ticket:
    sqlticket = session.get(SQLTicket, ticket_id)
    if not sqlticket:
        raise HTTPException(status_code=404, detail="Ticket not found")
    ticket = transform_to_ticket(sqlticket)
    return ticket


@router.post("/api/tickets/all")
def read_tickets(f: Filter, session: SessionDep) -> list[Ticket]:
    sqltickets = session.exec(select(SQLTicket)).all()
    if not sqltickets:
        raise HTTPException(status_code=404, detail="Tickets not found")
    for t in sqltickets:
        print(t)
    tickets = map(transform_to_ticket, sqltickets)
    return list(filter(f.apply, tickets))


@router.post("/api/tickets/root/{root_id}")
def get_api_tickets(f: Filter, root_id: int, session: SessionDep) -> list[Ticket]:
    sqltickets = session.exec(select(SQLTicket).where(SQLTicket.root_id == root_id)).all()
    if not sqltickets:
        raise HTTPException(status_code=404, detail="Ticket not found")
    tickets = map(transform_to_ticket, sqltickets)
    return list(filter(f.apply, tickets))


@router.put("api/tickets/{ticket_id}")
def update_ticket(ticket_id: int, ticket: Ticket, session: SessionDep):
    Ticket.model_validate(ticket)
    sql_ticket = transform_to_sql(ticket)
    db_ticket = session.get(SQLTicket, ticket_id)
    if not db_ticket:
        raise HTTPException(status_code=404, detail="Ticket not found")
    update_data = sql_ticket.dict(exclude_unset=True)
    for key, value in update_data.items():
        setattr(db_ticket, key, value)
    session.add(db_ticket)
    session.commit()
    session.refresh(db_ticket)
    return transform_to_ticket(db_ticket)
