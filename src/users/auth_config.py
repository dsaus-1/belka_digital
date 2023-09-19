from fastapi_users.authentication import BearerTransport, JWTStrategy, AuthenticationBackend
from fastapi_users import FastAPIUsers
from fastapi import Request

from src.users.models import User
from src.database import get_user_manager

from src.config import SECRET
import uuid


bearer_transport = BearerTransport(tokenUrl="users/jwt/login")

def get_jwt_strategy() -> JWTStrategy:
    return JWTStrategy(secret=SECRET, lifetime_seconds=3600)


auth_backend = AuthenticationBackend(
    name="jwt",
    transport=bearer_transport,
    get_strategy=get_jwt_strategy,
)


fastapi_users = FastAPIUsers[User, uuid.UUID](
    get_user_manager,
    [auth_backend],
)


current_active_user = fastapi_users.current_user(active=True)
