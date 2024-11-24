import shutil
from fastapi import APIRouter, UploadFile, Depends
from backend.config import settings
from backend.exception import NoPermitException
from backend.user.dao import UserDAO
from backend.user.models import User
from backend.user.dependecies import get_current_user
from backend.tasks.tasks import upload_profile_image

router = APIRouter(
    prefix='/images',
    tags=['Картинки'],
)

@router.post('/add_profile_image_to_s3')
async def add_profile_image_to_s3(file: UploadFile,
                                  current_user: User = Depends(get_current_user)):
    
    # if id_profile != current_user['id']:
    #     raise NoPermitException
    id_profile = current_user['id']

    file_path = f'backend/static/images/{id_profile}_profile.jpg'
    with open(file_path, 'wb+') as file_object:
        shutil.copyfileobj(file.file, file_object)

    file_url = f'https://storage.yandexcloud.net/{settings.BACKET_NAME}/{id_profile}_profile.jpg'
    await UserDAO.add_photo_url(id_profile, file_url)

    upload_profile_image.delay(file_path, id_profile)


@router.get('/get_url_image_profile_from_s3')
async def get_url_image_profile_from_s3(current_user: User = Depends(get_current_user)):
    id_profile = current_user['id']
    url_image = f'https://storage.yandexcloud.net/{settings.BACKET_NAME}/{id_profile}_profile.jpg'
    return url_image