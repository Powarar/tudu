from uuid import UUID
from sqlalchemy import select, update, delete, func
from sqlalchemy.dialects.postgresql import insert
from pydantic import EmailStr

from app.engines.postgres_storage import db_engine
from app.models.users import UserDB


async def user_exist_by_uuid(user_uuid: UUID) -> bool:
    subquery = select(UserDB.user_uuid).where(UserDB.user_uuid == user_uuid).exists()
    return await db_engine.execute(select(subquery))

async def get_user_by_uuid(user_id: UUID) -> UserDB | None:
    stmt = select(UserDB).where(UserDB.id == user_id)
    return await db_engine.select_one(stmt)

async def get_user_by_username(username: UUID) -> UserDB | None:
    stmt = select(UserDB).where(UserDB.username == username)
    return await db_engine.select_one(stmt)

async def update_user( user_uuid: UUID, user_data: dict):
    stmp = update(UserDB).where(UserDB.user_uuid == user_uuid).values(**user_data)
    await db_engine.execute(stmp, no_return=True)

async def create_or_update_user( user_data: dict) -> UserDB:
    stmt = (
    insert(UserDB)
    .values(**user_data)
    .on_conflict_do_update(
        index_elements=UserDB.__table__.primary_key.columns,
        set_={**user_data, UserDB.update_date: func.now()},
    )
    .returning(UserDB)
    )
    return await db_engine.execute(stmt)