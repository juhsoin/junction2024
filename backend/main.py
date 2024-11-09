from fastapi import FastAPI
from contextlib import asynccontextmanager

from .schemas.database_init import create_db_and_tables

from .routers import users, apis, tickets, update, comment


@asynccontextmanager
async def lifespan(app: FastAPI):
    # Code to run on startup, e.g., database connection
    create_db_and_tables()
    yield


app = FastAPI(lifespan=lifespan)


app.include_router(users.router)
app.include_router(apis.router)
app.include_router(tickets.router)
app.include_router(update.router)
app.include_router(comment.router)
