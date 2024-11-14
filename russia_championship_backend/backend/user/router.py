import random
from pydantic import EmailStr
from fastapi import APIRouter, Response, Depends, Request
from fastapi.templating import Jinja2Templates
from backend.config import settings
from backend.exception import VerifyPasswordException, ShortPasswordException
from backend.exception import HasExistingUserException, VerifyOldPasswordException
from backend.exception import OldAndNewPasswordEqException, ErrorLoginException
from backend.exception import NotEmailRegisterException, ErrorSinglemodeCode
from backend.user.schemas import SUserRegistartion, SChangePassword, SLoginUser
from backend.user.schemas import SCreateNewPassword
from backend.user.dao import UserDAO
from backend.user.auth import get_password_hash, authenticate_user, create_access_token, verify_password
from backend.user.dependecies import get_current_user
from backend.user.models import User
from backend.user.decorators import delete_password_and_role
from backend.tasks.tasks import send_new_password_on_email
from backend.client.google import get_google_user_info
from backend.client.yandex import get_yandex_user_info

templates = Jinja2Templates(directory="templates")

router = APIRouter(
    prefix='/user',
    tags=['Пользователи']
)


@router.post('/registr')
@delete_password_and_role
async def registr_user(user_data: SUserRegistartion):
    if user_data.password != user_data.password_verify:
        raise VerifyPasswordException
    
    if len(user_data.password) < 5:
        raise ShortPasswordException
    
    existing_user = await UserDAO.find_one_or_none(email = user_data.email)
    if existing_user:
        raise HasExistingUserException
    
    hashed_password = get_password_hash(user_data.password)

    created_user = await UserDAO.add(email=user_data.email,
                                     hashed_password=hashed_password)
    
    return created_user


@router.patch('/change_password')
@delete_password_and_role
async def change_password(user_data: SChangePassword,
                          current_user: User = Depends(get_current_user)):
    verify_old_password = await authenticate_user(current_user['email'],
                                                  user_data.old_password)
    
    if not verify_old_password:
        raise VerifyOldPasswordException
    
    if user_data.old_password == user_data.new_password:
        raise OldAndNewPasswordEqException
 
    if user_data.new_password != user_data.verify_new_password:
        raise VerifyPasswordException
    
    new_hashed_password = get_password_hash(user_data.new_password)

    changed_user = await UserDAO.update_by_id(current_user['id'],
                               hashed_password = new_hashed_password)
    return changed_user


@router.post('/login')
async def login_user(response: Response,
                     user_data: SLoginUser):
    user = await authenticate_user(user_data.email, user_data.password)
    if not user:
        raise ErrorLoginException
    access_token = create_access_token({'sub': str(user.id)})
    response.set_cookie('access_token', access_token, httponly=True)
    return access_token


@router.post('/logout')
async def logout_user(response: Response):
    response.delete_cookie('access_token')
    return 'ok'


@router.get('/me')
async def me_user(current_user: User = Depends(get_current_user)):
    return current_user


@router.get('/profile/me')
@delete_password_and_role
async def get_profile_by_id(current_user: User = Depends(get_current_user)):
    profile = await UserDAO.find_by_id(current_user['id'])
    return profile


@router.get('/profile/{profile_id}')
@delete_password_and_role
async def get_profile_by_id(profile_id: int):
    profile = await UserDAO.find_by_id(profile_id)
    return profile


@router.post('/dont_remember_password')
async def dont_remember_password(email: EmailStr):
    user = await UserDAO.find_one_or_none(email=email)
    if not user:
        raise NotEmailRegisterException
    
    new_password = random.randint(100000, 999999)

    new_hashed_password = get_password_hash(new_password)

    await UserDAO.update_by_id(user['id'],
                               hashed_password = new_hashed_password)
    
    send_new_password_on_email.delay(email, new_password)



@router.post('/verify_singlemode_code_from_mail')
async def verify_singlemode_code_from_mail(email: EmailStr,
                                           code: str):
    user = await UserDAO.find_one_or_none(email=email)
    return verify_password(code, user['hashed_password'])


@router.post('/create_new_password')
@delete_password_and_role
async def create_new_password(user_data: SCreateNewPassword):
    if user_data.new_password != user_data.verify_new_password:
        raise VerifyPasswordException
    user = await UserDAO.find_one_or_none(email=user_data.email)
    hashed_password = get_password_hash(user_data.new_password)
    user_changed = await UserDAO.update_by_id(user['id'],
                                        hashed_password=hashed_password)
    return user_changed


@router.get('/login/google')
async def login_google():
    redirect_url = settings.google_redirect_url
    return redirect_url


@router.get('/auth/google')
async def auth_google(code: str, response: Response, request: Request):
    print(code)
    user_data = get_google_user_info(code)
    
    user = await UserDAO.find_one_or_none(email=user_data.email)
    if user:
        access_token = create_access_token({'sub': str(user.id)})
        response.set_cookie('access_token', access_token, httponly=True)
        return templates.TemplateResponse(request=request,
                                          name="google.html")

    created_user = await UserDAO.add(email = user_data.email,
                                     google_access_token = user_data.access_token)
    access_token = create_access_token({'sub': str(created_user.id)})
    response.set_cookie('access_token', access_token, httponly=True)
    return created_user    


@router.get('/login/yandex')
async def login_yandex():
    redirect_url = settings.yandex_redirect_url
    return redirect_url


@router.get('/auth/yandex')
async def auth_yandex(code: str, response: Response):
    user_data = get_yandex_user_info(code)

    user = await UserDAO.find_one_or_none(email=user_data.email)
    if user:
        access_token = create_access_token({'sub': str(user.id)})
        response.set_cookie('access_token', access_token, httponly=True)
        return access_token

    created_user = await UserDAO.add(email = user_data.email,
                                     yandex_access_token = user_data.access_token)
    access_token = create_access_token({'sub': str(created_user.id)})
    response.set_cookie('access_token', access_token, httponly=True)
    return created_user 