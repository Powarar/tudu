from pydantic import BaseModel, ConfigDict
from uuid import UUID

class TaskBase(BaseModel):
    taskname: str
    description: str | None

class TaskCreate(TaskBase):
    pass
    
class TaskUpdate(TaskBase):
    taskname: str | None
    description: str | None
    is_completed: bool | None

class TaskRead(TaskBase):
    id: UUID
    is_completed: bool
    user_id: UUID
    model_config = ConfigDict(from_attributes=True)

class UserInTask(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    id: UUID
    username: str


class TaskReadWithUser(TaskRead):
    user: UserInTask