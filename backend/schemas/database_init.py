
from fastapi import Depends
from sqlmodel import Field, Session, SQLModel, create_engine
from typing import Annotated

sqlite_url = "sqlite:///db.sqlite"

connect_args = {"check_same_thread": False}
engine = create_engine(sqlite_url, connect_args=connect_args)


def create_db_and_tables():
    SQLModel.metadata.create_all(engine)
    return engine

def get_session():
    with Session(engine) as session:
        yield session


SessionDep = Annotated[Session, Depends(get_session)]
