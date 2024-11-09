from fastapi import FastAPI, HTTPException
from contextlib import asynccontextmanager

from .schemas.database_init import create_db_and_tables, SessionDep

from .routers import users, apis, tickets


@asynccontextmanager
async def lifespan(app: FastAPI):
    # Code to run on startup, e.g., database connection
    create_db_and_tables()
    yield


app = FastAPI(lifespan=lifespan)


app.include_router(users.router)
app.include_router(apis.router)
app.include_router(tickets.router)


