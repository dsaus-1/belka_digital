from sqlalchemy import insert
from datetime import datetime
import random
import pytz
from fastapi import BackgroundTasks

from src.database import async_session_maker
from src.statistics.models import General, DateMaxValue



async def trigger_max_value(datetime_now):
    async with async_session_maker() as session:
        stmt = insert(DateMaxValue).values(time=datetime_now)
        await session.execute(stmt)
        await session.commit()


async def add_data():
    datetime_now = datetime.now().astimezone(pytz.timezone('Europe/Moscow')).replace(tzinfo=None)
    value = round(random.uniform(0, 10), 5)

    async with async_session_maker() as session:
        stmt = insert(General).values(time=datetime_now, value=value)
        await session.execute(stmt)
        await session.commit()

    if value > 9.0:
        await trigger_max_value(datetime_now)

