import functools

def delete_password_and_role(func):
    @functools.wraps(func)
    async def wrapper(*args, **kwargs):
        user_row = await func(*args, **kwargs)
        user_dict = dict(user_row)
        exclude_key = ['hashed_password', 'role']
        for key in user_dict.copy():
            if key in exclude_key:
                del user_dict[key]
        return user_dict
    return wrapper