from ..schemas.database_init import SessionDep
from ..schemas.user import User

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


@router.get("/api/user/s{user_id}")
def read_user(user_id: int, session: SessionDep) -> User:
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
def delete_user(user_id: int, session: SessionDep):
    user = session.get(User, user_id)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    session.delete(user)
    session.commit()
    return {"ok": True}


@router.put("/api/users/{user_id}")
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

