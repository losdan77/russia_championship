import requests
from backend.config import settings
from backend.user.schemas import SYandexUserData


def get_yandex_user_info(code: str):
    access_token = _get_user_access_token(code=code)
    user_info = requests.get('https://login.yandex.ru/info?format=json',
                                 headers={'Authorization': f'OAuth {access_token}'})
    return SYandexUserData(**user_info.json(), 
                           access_token=access_token)

def _get_user_access_token(code: str) -> str:
    data = {
        'code': code,
        'client_id': settings.YANDEX_CLIENT_ID,
        'client_secret': settings.YANDEX_SECRET_KEY,
        'redirect_uri': settings.YANDEX_REDIRECT_URI,
        'grant_type': 'authorization_code',
    }

    headers = {
        'Content-Type': 'application/x-www-form-urlencoded',
    }
 
    response = requests.post(settings.YANDEX_TOKEN_URI, 
                             data=data,
                             headers=headers)
    return response.json()['access_token']