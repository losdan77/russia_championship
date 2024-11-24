from sqlalchemy import select, text, update
from sqlalchemy.orm import joinedload, selectinload
from backend.database import async_session_maker
from backend.user.models import User
from backend.event.models import City
from backend.dao.base import BaseDAO

class UserDAO(BaseDAO):
    model = User

    @classmethod
    async def find_by_id_for_profile(cls, id: int):
        async with async_session_maker() as session:
            query = select(User).filter_by(id=id).options(joinedload(User.city))                                                         
            result = await session.execute(query)
            return result.mappings().one_or_none()
        
    
    @classmethod
    async def add_photo_url(cls, id: int, photo_url: str):
        async with async_session_maker() as session:
            query = update(User).where(User.id == id).values(photo_url=photo_url)
            await session.execute(query)
            await session.commit()