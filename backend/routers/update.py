from ..schemas.update import SQLUpdate, Update
from ..schemas.filter import Filter
from ..schemas.database_init import SessionDep
from fastapi import APIRouter, HTTPException
from sqlmodel import select
import datetime


router = APIRouter()


def transform_to_sql(u: Update) -> SQLUpdate:
    sqlu: SQLTicket = u.__deepcopy__() # pyright: ignore
    if u.categories and len(u.categories) > 0:
        sqlu.categories = ",".join(u.categories) # pyright: ignore
    return sqlu

def transform_to_ticket(sqlu: SQLUpdate) -> Update:
    u: Ticket = SQLticket.__deepcopy__() # pyright: ignore
    if sqlu.categories and len(sqlu.categories) > 0:
        u.categories = sqlu.categories.split(",") # pyright: ignore
    return u


@router.post("/api/update/create/{ticket_id}")
def create_update(update: Update, ticket_id: str, session: SessionDep) -> Update:
    Update.model_validate(update)
    date = datetime.datetime.now()
    update.created_at = date.timestamp()
    update.updated_at = date.timestamp()
    update.id = datetime.datetime.now().strftime("%M%S")
    update.root_id = ticket_id
    sqlu = transform_to_sql(update)
    session.add(sqlu)
    session.commit()
    session.refresh(sqlu)
    return update


@router.post("/api/update/get/{ticket_id}")
def read_update(f: Filter, ticket_id: str, session: SessionDep) -> list[Update]:
    sqlupdates = session.exec(select(SQLUpdate).where(SQLUpdate.root_id == ticket_id)).all()
    if not sqlupdates:
        raise HTTPException(status_code=404, detail="Update not found")
    ups = map(transform_to_ticket, sqlupdates)
    return list(filter(f.apply, ups))
