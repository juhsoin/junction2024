from fastapi import FastAPI, HTTPException
from contextlib import asynccontextmanager
from backend.schemas.database_init import create_db_and_tables, SessionDep
from backend.schemas.ticket import Ticket
from sqlmodel import select

@asynccontextmanager
async def lifespan(app: FastAPI):
    # Code to run on startup, e.g., database connection
    create_db_and_tables()
    yield

app = FastAPI(lifespan=lifespan)

@app.post("/api/ticket/")
def create_hero(ticket: Ticket, session: SessionDep) -> Ticket:
    Ticket.model_validate(ticket)
    session.add(ticket)
    session.commit()
    session.refresh(ticket)
    return ticket

@app.get("/api/ticket/{ticket_id}")
def read_hero(ticket_id: int, session: SessionDep) -> Ticket:
    ticket = session.get(Ticket, ticket_id)
    if not ticket:
        raise HTTPException(status_code=404, detail="Ticket not found")
    return ticket

@app.get("/api/tickets/")
def read_heroes(session: SessionDep) -> list[Ticket]:
    tickets = session.exec(select(Ticket)).all()
    if not tickets:
        raise HTTPException(status_code=404, detail="Tickets not found")
    return tickets

@app.delete("/ticket/{ticket_id}")
def delete_hero(ticket_id: int, session: SessionDep):
    ticket = session.get(Ticket, ticket_id)
    if not ticket:
        raise HTTPException(status_code=404, detail="Ticket not found")
    session.delete(ticket)
    session.commit()
    return {"ok": True}

@app.put("/ticket/{ticket_id}")
def update_hero(ticket_id: int, ticket: Ticket, session: SessionDep):
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
