from sqlalchemy import select, insert, delete, update
from uuid import UUID
from app.engines.postgres_storage import db_engine
from app.models.tasks import TaskDB
from app.schemas.tasks import TaskCreate, TaskUpdate

async def create_task(task_data: TaskCreate, user_id: UUID):
    values = task_data.model_dump()
    values["user_id"] = user_id

    stmt = insert(TaskDB).values(**values).returning(TaskDB)
    return await db_engine.execute(stmt)

async def get_user_tasks(user_id: UUID):
    stmt = select(TaskDB).where(TaskDB.user_id == user_id)
    return await db_engine.execute(stmt, return_many=True)


async def delete_task(task_id: UUID, user_id: UUID):
    stmt = delete(TaskDB).where(TaskDB.id == task_id, TaskDB.user_id == user_id)
    await db_engine.execute(stmt, no_return=True)
