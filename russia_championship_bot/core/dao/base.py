from database import async_session_maker
from sqlalchemy import select


class BaseDAO:
    model = None

    @classmethod
    async def select(cls):
        async with async_session_maker() as session:
            query = select(cls.model.__table__)
            result = await session.execute(query)
            return result.mappings().all()