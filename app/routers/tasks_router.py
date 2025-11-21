from uuid import UUID
from fastapi import APIRouter, Depends

from app.schemas.tasks import TaskCreate, TaskRead
from app.auth.dependencies import get_current_user
from app.repositories.tasks import create_task, get_user_tasks, delete_task
from app.models.users import UserDB

router = APIRouter(prefix="/tasks", tags=["Tasks"])

@router.post("/", response_model=TaskRead)
async def add_task(
    task: TaskCreate, 
    user_id: UUID = Depends(get_current_user)
):
    return await create_task(task, user_id)

@router.get("/", response_model=list[TaskRead])
async def list_tasks(
    user_id: UUID = Depends(get_current_user)
):
    tasks = await get_user_tasks(user_id)
    if tasks is None:
        return []
    return tasks

@router.delete("/{task_id}")
async def remove_task(
    task_id: UUID,
    user_id: UUID = Depends(get_current_user)
):
    await delete_task(task_id, user_id)
    return {"ok": True}

