from datetime import date
from core.models.event import Events_notification, Events, Type_championship
from database import async_session_maker
from sqlalchemy import select
from core.dao.base import BaseDAO


class EventsNotificationDAO(BaseDAO):
    model = Events_notification

    @classmethod
    async def check_notification(cls, today_date: date):
        async with async_session_maker() as session:
            query = select(Events_notification.__table__).filter_by(count_days=today_date)
            result = await session.execute(query)
            return result.mappings().all()
        
class EventsDAO(BaseDAO):
    model = Events

class TypeChampionshipDAO(BaseDAO):
    model = Type_championship