from typing import List
from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select

from src.database import get_async_session, get_user_db
from src.users.auth_config import current_active_user
from src.statistics.schemas import GeneralSchemas
from src.statistics.models import General
from src.users.models import User


router = APIRouter(
    prefix='/statistics',
    tags=['Statistics']
)


@router.get('/')
async def get_statistics(
    limit: int = 50, offset: int = 0, 
    user: User = Depends(current_active_user),
    session: AsyncSession = Depends(get_async_session)):
    
    query = select(General).limit(limit).offset(offset)
    statistics_list = await session.execute(query)
    time = ''
    data = {}
    for i in statistics_list.scalars():

        if time == i.time.strftime("%d/%m/%y %H:%M"):
            data[time] += round(i.value, 5)

        else:
            time = i.time.strftime("%d/%m/%y %H:%M")
            data[time] = round(i.value, 5)

    return data
