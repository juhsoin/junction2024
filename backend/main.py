from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from contextlib import asynccontextmanager


from .schemas.database_init import create_db_and_tables

from .routers import users, apis, tickets, update, comment
from fastapi.staticfiles import StaticFiles
from fastapi.responses import HTMLResponse
from fastapi import Request


@asynccontextmanager
async def lifespan(app: FastAPI):
    # Code to run on startup, e.g., database connection
    create_db_and_tables()
    yield


app = FastAPI(lifespan=lifespan)


origins = [
    "http://localhost",
    "http://localhost:8000",
    "http://localhost:5173",
]

@app.middleware("http")
async def redirect_html_requests(request: Request, call_next):
    accept_header = request.headers.get("accept", "")
    if "text/html" in accept_header:
        print(request)
        return await read_index(request)
    response = await call_next(request)
    return response


app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(users.router)
app.include_router(apis.router)
app.include_router(tickets.router)
app.include_router(update.router)
app.include_router(comment.router)



@app.get("/", response_class=HTMLResponse)
async def read_index(request: Request):
    print(request.url)
    with open("static/index.html") as f:
        return HTMLResponse(content=f.read())


app.mount("/", StaticFiles(directory="static"), name="static")
