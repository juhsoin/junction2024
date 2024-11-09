from ..schemas.comment import Comment
from ..schemas.database_init import SessionDep
from fastapi import APIRouter, HTTPException
from sqlmodel import select
import datetime


router = APIRouter()


@router.post("/api/comment/{ticket_id}")
def create_comment(comment: Comment, ticket_id: str, session: SessionDep) -> Comment:
    Comment.model_validate(comment)
    comment.created_at = datetime.datetime.now().strftime("%Y-%m-%d--T%H-%M-%S")
    comment.updated_at = datetime.datetime.now().strftime("%Y-%m-%d--T%H-%M-%S")
    comment.id = datetime.datetime.now().strftime("%M%S")
    comment.root_id = ticket_id
    session.add(comment)
    session.commit()
    session.refresh(comment)
    print(comment)
    return comment


@router.get("/api/comment/{ticket_id}")
def read_comment(ticket_id: str, session: SessionDep) -> list[Comment]:
    comments = session.exec(select(Comment).where(Comment.root_id == ticket_id)).all()
    if not comments:
        raise HTTPException(status_code=404, detail="Comment not found")
    return list(comments)
