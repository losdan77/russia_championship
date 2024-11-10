from sqladmin import ModelView
from backend.user.models import User

class UserAdmin(ModelView, model=User):
    column_list = [User.id, User.email, User.role,
                   User.created_at,]
    column_details_exclude_list = [User.hashed_password]
    can_delete = False
    name = 'Пользователь'
    name_plural = 'Пользователи'
    icon = 'fa-solid fa-user'