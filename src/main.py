from fastapi import FastAPI
from apscheduler.schedulers.asyncio import AsyncIOScheduler

from src.users.auth_config import fastapi_users, auth_backend
from src.users.schemas import UserCreate, UserRead
from src.statistics.routers import router as statistics_router
from src.statistics.tasks import add_data

import asyncio


app = FastAPI()


scheduler = AsyncIOScheduler()
scheduler.add_job(add_data, 'interval', seconds=5)
scheduler.start()


app.include_router(
    fastapi_users.get_auth_router(auth_backend),
    prefix="/users/jwt",
    tags=["Users"],
)

app.include_router(
    fastapi_users.get_register_router(UserRead, UserCreate),
    prefix="/users",
    tags=["Users"],
)

app.include_router(statistics_router)
