from fastapi import status, HTTPException

NoAuthorization = HTTPException(
    status_code=status.HTTP_401_UNAUTHORIZED,
    detail='Пользователь неавторизован',
)

UserTokenException = HTTPException(
    status_code=status.HTTP_401_UNAUTHORIZED,
    detail='Ошибка токена доступа',
)

VerifyPasswordException = HTTPException(
    status_code=status.HTTP_409_CONFLICT,
    detail='Пароли не совпадают',
)

ShortPasswordException = HTTPException(
    status_code=status.HTTP_401_UNAUTHORIZED,
    detail='Короткий пароль',
)

HasExistingUserException = HTTPException(
    status_code=status.HTTP_401_UNAUTHORIZED,
    detail='Данный пользовать уже существует',
)

VerifyOldPasswordException = HTTPException(
    status_code=status.HTTP_409_CONFLICT,
    detail='Старый пароль не совпадает',
)

OldAndNewPasswordEqException = HTTPException(
    status_code=status.HTTP_409_CONFLICT,
    detail='Новый пароль должен отличаться от старого',
)

ErrorLoginException = HTTPException(
    status_code=status.HTTP_401_UNAUTHORIZED,
    detail='Неверный email или пароль',
)

NotEmailRegisterException = HTTPException(
    status_code=status.HTTP_404_NOT_FOUND,
    detail='Пользователя с таким email не существует'
)

ErrorSinglemodeCode = HTTPException(
    status_code=status.HTTP_404_NOT_FOUND,
    detail='Одноразовый код неверный',
)

StartEndDateException = HTTPException(
    status_code=status.HTTP_409_CONFLICT,
    detail='Ошибка ввода даты'
)

NoPermitException = HTTPException(
    status_code=status.HTTP_405_METHOD_NOT_ALLOWED,
    detail='Недостаточно прав'
)