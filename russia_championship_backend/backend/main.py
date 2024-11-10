from contextlib import asynccontextmanager
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi_cache import FastAPICache
from fastapi_cache.backends.redis import RedisBackend
from fastapi_cache.decorator import cache
from redis import asyncio as aioredis
from sqladmin import Admin
from backend.config import settings
from backend.database import engine_nullpool
from backend.admin.auth import authentication_backend
from backend.admin.view import UserAdmin
from backend.user.router import router as router_user

@asynccontextmanager
async def lifespan(app: FastAPI):
    redis = aioredis.from_url(f"redis://{settings.REDIS_HOST}:{settings.REDIS_PORT}")
    FastAPICache.init(RedisBackend(redis), prefix="cache")
    yield

app = FastAPI(title='Russia championship', lifespan=lifespan)

app.include_router(router_user)


admin = Admin(app, engine_nullpool, authentication_backend=authentication_backend)

admin.add_view(UserAdmin)


origins = [
    'http://localhost:8000',
    '*',
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=['GET', 'POST', 'OPTIONS', 'DELETE', 'PATCH', 'PUT'],
    allow_headers=['Content-Type',
                   'Set-Cookie',
                   'Access-Control-Allow-Headers',
                   'Access-Control-Allow-Origin',
                   'Authorization'],
)