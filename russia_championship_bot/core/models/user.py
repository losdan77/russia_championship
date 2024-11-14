from sqlalchemy import Index, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship
from database import Base, intpk, str_not_null, str_null, created_at

class User(Base):
    __tablename__ = 'user'

    id: Mapped[intpk]
    email: Mapped[str_not_null]
    hashed_password: Mapped[str_null]
    role: Mapped[str_null]
    created_at: Mapped[created_at]
    photo_url: Mapped[str_null]
    google_access_token: Mapped[str_null]
    yandex_access_token: Mapped[str_null]
    
    __table_args__ = (
        Index('email_index', 'email'),
    )

    def __str__(self):
        return f'{self.email}'