from database import async_session_maker
from sqlalchemy import select, update, insert


class BaseDAO:
    model = None

    @classmethod
    async def select(cls):
        async with async_session_maker() as session:
            query = select(cls.model.__table__)
            result = await session.execute(query)
            return result.mappings().all()
        
    
    @classmethod
    async def find_by(cls, **filter_by):
        async with async_session_maker() as session:
            query = select(cls.model.__table__.columns).filter_by(**filter_by)
            result = await session.execute(query)
            return result.mappings().one_or_none()
        
    
    @classmethod
    async def update_by_id(cls, id: int, **data):
        async with async_session_maker() as session:
            query = update(cls.model).returning(cls.model.__table__).where(cls.model.id==id).values(data)
            result = await session.execute(query)
            await session.commit()
            return result.mappings().one()
        
    
    @classmethod
    async def add(cls, **data):
        async with async_session_maker() as session:
            query = insert(cls.model).returning(cls.model.__table__).values(**data)
            result = await session.execute(query)
            await session.commit()
            return result.mappings().one()
        

   