from contextlib import asynccontextmanager
from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from .routers.auth_router import router as auth_router
from .routers.tasks_router import router as task_router
from .engines.postgres_storage import db_engine
from .models.users import UserDB
from .models.tasks import TaskDB

async def init_postgres() -> None:
    await db_engine.create_tables()

@asynccontextmanager
async def lifespan(app: FastAPI):
    await init_postgres()
    yield

app = FastAPI(lifespan=lifespan)
app.mount("/static", StaticFiles(directory="static", html=True), name="static")

@app.get("/")
def homepage() -> dict:
    return {"message": "Привет!"}

app.include_router(auth_router)
app.include_router(task_router)
