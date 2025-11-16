from contextlib import asynccontextmanager

from fastapi import FastAPI
import uvicorn

from .routers.auth_router import router as auth_router
from .engines.postgres_storage import db_engine, PostgresEngine

from .models.users import UserDB
from .models.tasks import TaskDB

async def init_postgres() -> None:
    await db_engine.create_tables()



@asynccontextmanager
async def lifespan(app: FastAPI):  # noqa
    await init_postgres()
    yield

app = FastAPI(lifespan=lifespan)

@app.get("/")
def homepage() -> dict:
    return {"message": "Привет!"}

app.include_router(auth_router)

# uvicorn.run(app, port=8000)