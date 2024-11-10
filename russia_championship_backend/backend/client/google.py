import requests
from backend.config import settings
from backend.user.schemas import SGoogleUserData

def get_google_user_info(code: str) -> SGoogleUserData:
    access_token = _get_user_access_token(code=code)
    user_info = requests.get('https://www.googleapis.com/oauth2/v1/userinfo',
                                 headers={'Authorization': f'Bearer {access_token}'})
    return SGoogleUserData(**user_info.json(),
                            access_token=access_token)

def _get_user_access_token(code: str) -> str:
        data = {
            'code': code,
            'client_id': settings.GOOGLE_CLIENT_ID,
            'client_secret': settings.GOOGLE_SECRET_KEY,
            'redirect_uri': settings.GOOGLE_REDIRECT_URI_BACK,
            'grant_type': 'authorization_code',
            'scope': 'openid email profile',  
            'include_granted_scopes': 'true'
        }

        headers = {
            'Content-Type': 'application/x-www-form-urlencoded',
        }
 
        response = requests.post(settings.GOOGLE_TOKEN_URI, 
                                 data=data,
                                 headers=headers)
        
        return response.json()['access_token']
      
