from pydantic import BaseModel, EmailStr, Field

class SUserRegistartion(BaseModel):
    email: EmailStr
    password: str
    password_verify: str

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
