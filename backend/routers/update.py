from ..schemas.update import Update
from ..schemas.filter import Filter
from ..schemas.database_init import SessionDep
from fastapi import APIRouter, HTTPException
from sqlmodel import select
import datetime


router = APIRouter()


@router.post("/api/update/create/{ticket_id}")
def create_update(update: Update, ticket_id: str, session: SessionDep) -> Update:
    Update.model_validate(update)
    date = datetime.datetime.now()
    update.created_at = date.timestamp()
    update.updated_at = date.timestamp()
    update.id = datetime.datetime.now().strftime("%M%S")
    update.root_id = ticket_id
    session.add(update)
    session.commit()
    session.refresh(update)
    return update


@router.post("/api/update/get/{ticket_id}")
def read_update(f: Filter, ticket_id: str, session: SessionDep) -> list[Update]:
    updates = session.exec(select(Update).where(Update.root_id == ticket_id)).all()
    if not updates:
        raise HTTPException(status_code=404, detail="Update not found")
    return list(filter(f.apply, updates))
