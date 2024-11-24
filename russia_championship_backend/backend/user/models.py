from sqlalchemy import Index, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship
from datetime import datetime
from backend.database import Base, intpk, str_not_null, str_null, created_at
from backend.event.models import City

class User(Base):
    __tablename__ = 'user'

    id: Mapped[intpk]
    FIO: Mapped[str_null]
    email: Mapped[str_not_null] = mapped_column(unique=True)
    hashed_password: Mapped[str_null]
    single_mode_code: Mapped[str_null]
    role: Mapped[str_null]
    created_at: Mapped[created_at]
    photo_url: Mapped[str_null]
    google_access_token: Mapped[str_null]
    yandex_access_token: Mapped[str_null]
    telegram_id: Mapped[str_null]
    is_coach: Mapped[bool] = mapped_column(nullable=False,
                                           default=False)
    birthday_date: Mapped[datetime] = mapped_column(nullable=True)
    phone_number: Mapped[str_null]
    about: Mapped[str_null]
    id_city: Mapped[int] = mapped_column(ForeignKey('city.id'),
                                         nullable=True) 

    city: Mapped[list['City']] = relationship(back_populates='users')
    event: Mapped[list['Events']] = relationship(
        back_populates='user',
        secondary='events_notification'
        )
    
    __table_args__ = (
        Index('email_index', 'email'),
    )

    def __str__(self):
        return f'{self.email}'