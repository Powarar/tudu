from sqlalchemy import ForeignKey, UUID
from sqlalchemy.orm import relationship, Mapped, mapped_column
from uuid import uuid4

from app.models.base import BaseDB

class TaskDB(BaseDB):
    __tablename__ = "tasks"

    id: Mapped[UUID] = mapped_column(UUID(as_uuid=True), primary_key=True, default=uuid4)
    title: Mapped[str]
    description: Mapped[str | None]
    is_completed: Mapped[bool] = mapped_column(default=False)

    user_id: Mapped[UUID] = mapped_column(ForeignKey('users.id'))
    user: Mapped["UserDB"] = relationship(back_populates="tasks")