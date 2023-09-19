import uuid
from fastapi_users.schemas import BaseUser, BaseUserCreate


class UserRead(BaseUser[uuid.UUID]):
    pass


class UserCreate(BaseUserCreate):
    pass