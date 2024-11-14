from core.dao.base import BaseDAO
from core.models.user import User

class UserDAO(BaseDAO):
    model = User
