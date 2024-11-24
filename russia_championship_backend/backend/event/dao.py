from sqlalchemy import select, and_, text
from sqlalchemy.orm import joinedload, selectinload
from datetime import datetime, date
from backend.database import async_session_maker
from backend.event.models import Countrys, Subjects, City, Discipline
from backend.event.models import Type_championship, Type_sport, Events, Sex
from backend.event.models import Events_Discipline, Events_Sex, Events_notification
from backend.dao.base import BaseDAO

class CountrysDAO(BaseDAO):
    model = Countrys

class SubjectsDAO(BaseDAO):
    model = Subjects

class CityDAO(BaseDAO):
    model = City

class TypeChampionshipDAO(BaseDAO):
    model = Type_championship

class TypeSportDAO(BaseDAO):
    model = Type_sport

class EventsDAO(BaseDAO):
    model = Events

    @staticmethod
    async def find_all_count_values():
        async with async_session_maker() as session:
            query = 'select distinct count from events'
            result = await session.execute(text(query))
            return result.mappings().all()
        
    @classmethod
    async def find_one(cls, event_id: str):
        async with async_session_maker() as session:
            query = (
                            select(Events)
                            .options(
                                # Загружаем связанные объекты
                                joinedload(Events.city),
                                joinedload(Events.type_championship),
                                joinedload(Events.type_sport),
                                # joinedload(City.subjects),
                                selectinload(Events.sex),  # через таблицу events_sex
                                selectinload(Events.discipline),  # через таблицу events_discipline
                                    )
                            ).where(
                                Events.id == event_id
                            )
            result = await session.execute(query)
            return result.mappings().one_or_none() 

    @classmethod
    async def find_all(cls, 
                       subject: str, 
                       city: list, 
                       type_championship_name: list,
                       type_sport_name: list,
                       sex_name: list,
                       discipline_name: list,
                       count_values: list,
                       date_start: datetime,
                       date_end: datetime):
        async with async_session_maker() as session:
            query = (
                            select(Events)
                            .options(
                                # Загружаем связанные объекты
                                joinedload(Events.city),
                                joinedload(Events.type_championship),
                                joinedload(Events.type_sport),
                                # joinedload(City.subjects),
                                selectinload(Events.sex),  # через таблицу events_sex
                                selectinload(Events.discipline),  # через таблицу events_discipline
                                    )
                            ).where(
                                and_(
                                True if not subject else Events.city.has(City.subjects.has(subject_name = subject)),
                                True if not city else Events.city.has(City.city_name.in_(city)),
                                True if not type_championship_name else Events.type_championship.has(Type_championship.type_name.in_(type_championship_name)),
                                True if not type_sport_name else Events.type_sport.has(Type_sport.type_name.in_(type_sport_name)),
                                True if not sex_name else Events.sex.any(Sex.sex.in_(sex_name)),
                                True if not discipline_name else Events.discipline.any(Discipline.discipline_name.in_(discipline_name)),
                                True if not count_values else Events.count.in_(count_values),
                                True if not date_start else Events.date_start >= date_start,
                                True if not date_end else Events.date_end <= date_end,
                                )
                            )
            result = await session.execute(query)
            return result.mappings().all() 

class SexDAO(BaseDAO):
    model = Sex

class DisciplineDAO(BaseDAO):
    model = Discipline

class EventsSexDAO(BaseDAO):
    model = Events_Sex

class EventsDisciplineDAO(BaseDAO):
    model = Events_Discipline

class EventsNotificationDAO(BaseDAO):
    model = Events_notification

    @classmethod
    async def check_notification(cls, today_date: date):
        async with async_session_maker() as session:
            query = select(Events_notification.__table__).filter_by(count_days=today_date)
            result = await session.execute(query)
            return result.mappings().all()