
from backend.schemas.api import Api
from backend.schemas.database_init import  SessionDep
import datetime
from fastapi import APIRouter

router = APIRouter()


@router.post("/api/apis")
def create_api(api: Api, session: SessionDep) -> Api:
    session.add(api)
    api.created_at = datetime.datetime.now().strftime("%Y-%m-%d--T%H-%M-%S")
    api.updated_at = datetime.datetime.now().strftime("%Y-%m-%d--T%H-%M-%S")
    api.id = datetime.datetime.now().strftime("%M%S")
    session.commit()
    session.refresh(api)
    print(api)
    return api