from ..schemas.api import Api
from ..schemas.database_init import SessionDep
import datetime
from fastapi import APIRouter, HTTPException
from sqlmodel import select
import datetime

router = APIRouter()


@router.post("/api/apis")
def create_api(api: Api, session: SessionDep) -> Api:
    session.add(api)
    date = datetime.datetime.now()
    api.created_at = date.timestamp()
    api.updated_at = date.timestamp()
    api.id = datetime.datetime.now().strftime("%M%S")
    session.commit()
    session.refresh(api)
    print(api)
    return api


@router.get("/api/apis")
def get_all_apis(session: SessionDep) -> list[Api]:
    apis = session.exec(select(Api)).all()
    if not apis:
        raise HTTPException(status_code=404, detail="Comment not found")
    return list(apis)
