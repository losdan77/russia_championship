from pydantic import BaseModel, EmailStr, Field

class SUserRegistartion(BaseModel):
    email: EmailStr
    password: str
    password_verify: str
    FIO: str | None = None
    is_coach: bool
    phone_number: str | None = None
    photo_url: str | None = None
    city: str | None = None

class SChangePassword(BaseModel):
    old_password: str
    new_password: str
    verify_new_password: str

class SLoginUser(BaseModel):
    email: EmailStr
    password: str

class SCreateNewPassword(BaseModel):
    email: str
    new_password: str
    verify_new_password: str

class SGoogleUserData(BaseModel):
    id: int
    email: str
    verified_email: bool | None = None
    name: str | None = None
    given_name: str | None = None
    picture: str | None = None
    access_token: str

class SYandexUserData(BaseModel):
    id: int
    login: str
    name: str = Field(alias='real_name')
    email: str = Field(alias='default_email')
    access_token: str

class SUserProfileChange(BaseModel):
    FIO: str | None = None
    is_coach: bool
    birthday_date: str | None = None
    phone_number: str | None = None
    about: str | None = None
