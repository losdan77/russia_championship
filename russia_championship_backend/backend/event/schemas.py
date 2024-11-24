from datetime import datetime, date
from pydantic import BaseModel, EmailStr, Field

class SFilter(BaseModel):
    subject: str | None = None
    city: str | None = None
    type_championship_name: str | None = None
    type_sport_name: str | None = None
    sex_name: str | None = None
    discipline_name: str | None = None
    count_values: str | None = None
    date_start: date | None = None
    date_end: date | None = None

class SSubscribe(BaseModel):
    event_id: str
    count_day: int