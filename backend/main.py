from fastapi import FastAPI, HTTPException
from contextlib import asynccontextmanager
from backend.schemas.database_init import create_db_and_tables, SessionDep
from backend.schemas.ticket import Ticket

@asynccontextmanager
async def lifespan(app: FastAPI):
    # Code to run on startup, e.g., database connection
    create_db_and_tables()
    yield
    # Code to run on shutdown, e.g., closing database connection
    app.state.db.close()

app = FastAPI(lifespan=lifespan)

@app.post("/api/ticket/")
def create_hero(ticket: Ticket, session: SessionDep) -> Ticket:
    session.add(ticket)
    session.commit()
    session.refresh(ticket)
    return ticket

@app.get("/api/ticket/{ticket_id}")
def read_hero(ticket_id: int, session: SessionDep) -> Ticket:
    ticket = session.get(Ticket, ticket_id)
    if not ticket:
        raise HTTPException(status_code=404, detail="Hero not found")
    return ticket

@app.delete("/heroes/{ticket_id}")
def delete_hero(ticket_id: int, session: SessionDep):
    ticket = session.get(Ticket, ticket_id)
    if not ticket:
        raise HTTPException(status_code=404, detail="Hero not found")
    session.delete(ticket)
    session.commit()
    return {"ok": True}