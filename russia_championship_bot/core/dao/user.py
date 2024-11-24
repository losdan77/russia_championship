from sqlalchemy import text
from core.dao.base import BaseDAO
from core.models.user import User
from database import async_session_maker

class UserDAO(BaseDAO):
    model = User


    @classmethod
    async def get_list_user(cls):
        async with async_session_maker() as session:
            query = 'select telegram_id from "user" where telegram_id is not null'
            result = await session.execute(text(query))
            return result.mappings().all()