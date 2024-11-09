from ..schemas.update import Update
from ..schemas.database_init import SessionDep
from fastapi import APIRouter, HTTPException
from sqlmodel import select
import datetime


router = APIRouter()


@router.post("/api/update/{ticket_id}")
def create_update(update: Update, ticket_id: str, session: SessionDep) -> Update:
    Update.model_validate(update)
    update.created_at = datetime.datetime.now().strftime("%Y-%m-%d--T%H-%M-%S")
    update.updated_at = datetime.datetime.now().strftime("%Y-%m-%d--T%H-%M-%S")
    update.id = datetime.datetime.now().strftime("%M%S")
    update.root_id = ticket_id
    session.add(update)
    session.commit()
    session.refresh(update)
    return update


@router.get("/api/update/{ticket_id}")
def read_update(ticket_id: str, session: SessionDep) -> list[Update]:
    updates = session.exec(select(Update).where(Update.root_id == ticket_id)).all()
    if not updates:
        raise HTTPException(status_code=404, detail="Update not found")
    return list(updates)
