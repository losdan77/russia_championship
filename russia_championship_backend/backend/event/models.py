from sqlalchemy import Index, ForeignKey, Date
from sqlalchemy.orm import Mapped, mapped_column, relationship
from datetime import datetime
from backend.database import Base, intpk, str_not_null, str_null, created_at


class Countrys(Base):
    __tablename__ = 'countrys'

    id: Mapped[intpk]
    country_name: Mapped[str_null] = mapped_column(unique=True)

    subjects: Mapped[list['Subjects']] = relationship(back_populates='countrys')

    def __str__(self):
        return f'{self.country_name}'


class Subjects(Base):
    __tablename__ = 'subjects'

    id: Mapped[intpk]
    subject_name: Mapped[str_null] = mapped_column(unique=True)
    id_country: Mapped[int] = mapped_column(ForeignKey('countrys.id'),
                                            nullable=False)
    
    countrys: Mapped[list['Countrys']] = relationship(back_populates='subjects')
    city: Mapped[list['City']] = relationship(back_populates='subjects')

    def __str__(self):
        return f'{self.subject_name}'


class City(Base):
    __tablename__ = 'city'

    id: Mapped[intpk]
    city_name: Mapped[str_null] = mapped_column(unique=True)
    id_subject: Mapped[int] = mapped_column(ForeignKey('subjects.id'),
                                            nullable=False)
    
    subjects: Mapped[list['Subjects']] = relationship(back_populates='city')
    users: Mapped[list['User']] = relationship(back_populates='city')
    event: Mapped[list['Events']] = relationship(back_populates='city')
    
    __table_args__ = (
        Index('city_name_index', 'city_name'),
    )
    
    def __str__(self):
        return f'{self.city_name}'
    

class Sex(Base):
    __tablename__ = 'sex'

    id: Mapped[intpk]
    sex: Mapped[str_null] = mapped_column(unique=True)

    event: Mapped[list['Events']] = relationship(
        back_populates='sex',
        secondary='events_sex',
        )

    def __str__(self):
        return f'{self.sex}' 
    

class Type_championship(Base):
    __tablename__ = 'type_championship'

    id: Mapped[intpk]
    type_name: Mapped[str_null] = mapped_column(unique=True)

    event: Mapped[list['Events']] = relationship(back_populates='type_championship')

    def __str__(self):
        return f'{self.type_name}'
    

class Type_sport(Base):
    __tablename__ = 'type_sport'

    id: Mapped[intpk]
    type_name: Mapped[str_null] = mapped_column(unique=True)

    event: Mapped[list['Events']] = relationship(back_populates='type_sport')

    def __str__(self):
        return f'{self.type_name}'
    

class Discipline(Base):
    __tablename__ = 'discipline'

    id: Mapped[intpk]
    discipline_name: Mapped[str_null] = mapped_column(unique=True)

    event: Mapped[list['Events']] = relationship(
        back_populates='discipline',
        secondary='events_discipline',
        )

    def __str__(self):
        return f'{self.discipline_name}'
    

class Events(Base):
    __tablename__ = 'events'

    id: Mapped[str] = mapped_column(primary_key=True)
    date_start: Mapped[datetime] = mapped_column(Date, nullable=True)
    date_end: Mapped[datetime] = mapped_column(Date, nullable=True)
    photo_url: Mapped[str_null]
    count: Mapped[str_null] 

    id_type_championship: Mapped[int] = mapped_column(ForeignKey('type_championship.id'),
                                                      nullable=True)
    id_type_sport: Mapped[int] = mapped_column(ForeignKey('type_sport.id'),
                                               nullable=True)
    id_city: Mapped[int] = mapped_column(ForeignKey('city.id'),
                                         nullable=True)
    
    type_championship: Mapped[list['Type_championship']] = relationship(back_populates='event')
    type_sport: Mapped[list['Type_sport']] = relationship(back_populates='event')
    city: Mapped[list['City']] = relationship(back_populates='event')
    discipline: Mapped[list['Discipline']] = relationship(
        back_populates='event',
        secondary='events_discipline',
        )
    sex: Mapped[list['Sex']] = relationship(
        back_populates='event',
        secondary='events_sex',
        )
    user: Mapped[list['User']] = relationship(
        back_populates='event',
        secondary='events_notification'
        )
    
    __table_args__ = (
        Index('type_sport_index', 'id_type_sport'),
    )

    def __str__(self):
        return f'{self.type_sport}'
    

class Events_notification(Base):
    __tablename__ = 'events_notification'

    event_id: Mapped[str] = mapped_column(
        ForeignKey('events.id', ondelete='CASCADE'),
        primary_key=True,
    )

    user_id: Mapped[str] = mapped_column(
        ForeignKey('user.id', ondelete='CASCADE'),
        primary_key=True,
    )

    count_days: Mapped[datetime] = mapped_column(Date, nullable=True)


class Events_Sex(Base):
    __tablename__ = 'events_sex'

    event_id: Mapped[str] = mapped_column(
        ForeignKey('events.id', ondelete='CASCADE'),
        primary_key=True,
    )

    sex_id: Mapped[int] = mapped_column(
        ForeignKey('sex.id', ondelete='CASCADE'),
        primary_key=True,
    )


class Events_Discipline(Base):
    __tablename__ = 'events_discipline'

    event_id: Mapped[str] = mapped_column(
        ForeignKey('events.id', ondelete='CASCADE'),
        primary_key=True,
    )

    discipline_id: Mapped[id] = mapped_column(
        ForeignKey('discipline.id', ondelete='CASCADE'),
        primary_key=True,
    )
