from sqlalchemy import select
from backend.database import async_session_maker
from backend.user.models import User
from backend.dao.base import BaseDAO

class UserDAO(BaseDAO):
    model = User

    