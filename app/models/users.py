from sqlalchemy.orm import Mapped, mapped_column, relationship
from uuid import uuid4
from sqlalchemy import UUID

from app.models.base import BaseDB


class UserDB(BaseDB):
    __tablename__ = "users"

    id: Mapped[UUID] = mapped_column(UUID(as_uuid=True), primary_key=True, default=uuid4)
    username: Mapped[str] = mapped_column(unique=True)
    password: Mapped[str]
    first_name: Mapped[str]
    last_name: Mapped[str]
    
    tasks: Mapped[list["TaskDB"]] = relationship(back_populates="user")