from ..schemas.comment import Comment
from ..schemas.filter import Filter
from ..schemas.database_init import SessionDep
from fastapi import APIRouter, HTTPException
from sqlmodel import select
import datetime


router = APIRouter()


@router.post("/api/comment/create/{ticket_id}")
def create_comment(comment: Comment, ticket_id: str, session: SessionDep) -> Comment:
    Comment.model_validate(comment)
    date = datetime.datetime.now()
    comment.created_at = date.timestamp()
    comment.updated_at = date.timestamp()
    comment.id = datetime.datetime.now().strftime("%M%S")
    comment.root_id = ticket_id
    session.add(comment)
    session.commit()
    session.refresh(comment)
    print(comment)
    return comment


@router.post("/api/comment/get/{ticket_id}")
def read_comment(f: Filter, ticket_id: str, session: SessionDep) -> list[Comment]:
    comments = session.exec(select(Comment).where(Comment.root_id == ticket_id)).all()
    if not comments:
        raise HTTPException(status_code=404, detail="Comment not found")
    return list(filter(f.apply, comments))
