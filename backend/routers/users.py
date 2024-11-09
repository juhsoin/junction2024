from ..schemas.database_init import SessionDep
from ..schemas.user import User
from ..schemas.ticket_subscription import TicketSubscription
from ..schemas.ticket import Ticket

import datetime
from fastapi import APIRouter, HTTPException
from sqlmodel import select


router = APIRouter()


@router.post("/api/users/")
def create_user(user: User, session: SessionDep) -> User:
    User.model_validate(user)
    session.add(user)
    session.commit()
    session.refresh(user)
    return user


@router.get("/api/users/{user_id}")
def read_user(user_id: str, session: SessionDep) -> User:
    user = session.get(User, user_id)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return user


@router.get("/api/users/")
def read_users(session: SessionDep) -> list[User]:
    users = session.exec(select(User)).all()
    if not users:
        raise HTTPException(status_code=404, detail="Users not found")
    return list(users)


@router.delete("/api/users/{user_id}")
def delete_user(user_id: str, session: SessionDep):
    user = session.get(User, user_id)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    session.delete(user)
    session.commit()
    return {"ok": True}


@router.put("/api/users/{user_id}")
def update_user(user_id: str, user: User, session: SessionDep):
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


@router.get("/api/users/{user_id}/tickets")
def read_user_tickets(user_id: str, session: SessionDep) -> list[Ticket]:
    user = session.get(User, user_id)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    
    tickets = session.exec(
        select(Ticket)
        .select_from(Ticket)
        .join(TicketSubscription, Ticket.id == TicketSubscription.ticket_id)
        .where(TicketSubscription.user_id == user_id)
    ).all()
    
    if not tickets:
        raise HTTPException(status_code=404, detail="Tickets not found")
    
    return tickets


@router.post("/api/users/{user_id}/subscribe/{ticket_id}")
def subscribe_user_to_ticket(user_id: str, ticket_id: str, session: SessionDep):
    user = session.get(User, user_id)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    
    ticket = session.get(Ticket, ticket_id)
    if not ticket:
        raise HTTPException(status_code=404, detail="Ticket not found")
    
    id = datetime.datetime.now().strftime("%M%S")
    subscription = TicketSubscription(id=id, user_id=user_id, ticket_id=str(ticket_id))
    session.add(subscription)
    session.commit()
    session.refresh(subscription)
    
    return subscription