from pydantic import BaseModel, ConfigDict, Field
from uuid import UUID
from .tasks import TaskRead


class UserBase(BaseModel):
    username: str = Field(min_length=4, max_length=15)
    first_name: str = Field(min_length=4, max_length=15)
    last_name: str = Field(min_length=4, max_length=15)



class UserLogin(BaseModel):
    username: str = Field(min_length=4, max_length=15)
    password: str = Field(min_length=6, max_length=20)

class UserRegister(UserBase):
    password: str = Field(min_length=6, max_length=20)



class UserRead(UserBase):
    model_config = ConfigDict(from_attributes=True)
    id: UUID

class UserReadWithTasks(UserRead):
    tasks: list[TaskRead] = []

class UserUpdate(UserBase):
    username: str | None
    first_name: str | None
    last_name: str | None
    password: str | None
    