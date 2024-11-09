from ..schemas.database_init import SessionDep
from ..schemas.user import User
from ..schemas.ticket_subscription import TicketSubscription
from ..schemas.ticket import Ticket

from fastapi import APIRouter, HTTPException
from sqlmodel import select
import datetime


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


@router.get("/api/users/{user_id}/tickets")
def read_user_tickets(user_id: str, session: SessionDep) -> list[Ticket]:
    user = session.get(User, user_id)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")

    tickets = session.exec(
        select(Ticket).select_from(Ticket).join(TicketSubscription)
    ).all()

    return list(tickets)


@router.post("/api/users/{user_id}/subscribe/{ticket_id}")
def subscribe_user_to_ticket(user_id: str, ticket_id: str, session: SessionDep):
    user = session.get(User, user_id)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")

    ticket = session.get(Ticket, ticket_id)
    if not ticket:
        raise HTTPException(status_code=404, detail="Ticket not found")

    subscription = session.exec(
        select(TicketSubscription)
        .where(TicketSubscription.user_id == user_id)
        .where(TicketSubscription.ticket_id == ticket_id)
    ).all()

    if subscription:
        print("Already subscribed")
        return subscription

    id = datetime.datetime.now().strftime("%M%S")
    subscription = TicketSubscription(id=id, user_id=user_id, ticket_id=str(ticket_id))
    session.add(subscription)
    session.commit()
    session.refresh(subscription)

    return subscription


@router.delete("/api/users/{user_id}/subscribe/{ticket_id}")
def unsubscribe_user_from_ticket(user_id: str, ticket_id: str, session: SessionDep):
    subscription = session.exec(
        select(TicketSubscription).where(
            TicketSubscription.user_id == user_id
            and TicketSubscription.ticket_id == ticket_id
        )
    ).all()

    if subscription:
        res = subscription[0]
        session.delete(res)
        session.commit()
        return subscription
    else:
        raise HTTPException(status_code=404, detail="User not found")
