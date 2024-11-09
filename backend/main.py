from fastapi import FastAPI, HTTPException
from contextlib import asynccontextmanager
from backend.schemas.database_init import create_db_and_tables, SessionDep
from sqlmodel import select

#schema imports
from backend.schemas.ticket import Ticket
from backend.schemas.user import User


@asynccontextmanager
async def lifespan(app: FastAPI):
    # Code to run on startup, e.g., database connection
    create_db_and_tables()
    yield

app = FastAPI(lifespan=lifespan)


@app.post("/api/user/")
def create_user(user: User, session: SessionDep) -> User:
    User.model_validate(user)
    session.add(user)
    session.commit()
    session.refresh(user)
    return user


@app.get("/api/user/{user_id}")
def read_user(user_id: int, session: SessionDep) -> User:
    user = session.get(User, user_id)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return user


@app.get("/api/users/")
def read_users(session: SessionDep) -> list[User]:
    users = session.exec(select(User)).all()
    if not users:
        raise HTTPException(status_code=404, detail="Users not found")
    return users


@app.delete("/api/user/{user_id}")
def delete_user(user_id: int, session: SessionDep):
    user = session.get(User, user_id)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    session.delete(user)
    session.commit()
    return {"ok": True}


@app.put("/api/user/{user_id}")
def update_user(user_id: int, user: User, session: SessionDep):
    User.model_validate(user)
    db_user = session.get(User, user_id)
    if not db_user:
        raise HTTPException(status_code=404, detail="User not found")
    update_data = user.dict(exclude_unset=True)
    for key, value in update_data.items():
        setattr(db_user, key, value)
    session.add(db_user)
    session.commit()
    session.refresh(db_user)
    return db_user


@app.post("/api/ticket/")
def create_ticket(ticket: Ticket, session: SessionDep) -> Ticket:
    Ticket.model_validate(ticket)
    session.add(ticket)
    session.commit()
    session.refresh(ticket)
    return ticket


@app.get("/api/ticket/{ticket_id}")
def read_ticket(ticket_id: int, session: SessionDep) -> Ticket:
    ticket = session.get(Ticket, ticket_id)
    if not ticket:
        raise HTTPException(status_code=404, detail="Ticket not found")
    return ticket


@app.get("/api/tickets/")
def read_tickets(session: SessionDep) -> list[Ticket]:
    tickets = session.exec(select(Ticket)).all()
    if not tickets:
        raise HTTPException(status_code=404, detail="Tickets not found")
    return tickets


@app.delete("/ticket/{ticket_id}")
def delete_ticket(ticket_id: int, session: SessionDep):
    ticket = session.get(Ticket, ticket_id)
    if not ticket:
        raise HTTPException(status_code=404, detail="Ticket not found")
    session.delete(ticket)
    session.commit()
    return {"ok": True}


@app.put("/ticket/{ticket_id}")
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