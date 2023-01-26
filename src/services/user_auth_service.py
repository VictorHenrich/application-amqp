from typing import Mapping, Any
from dataclasses import dataclass
from jwt import PyJWT
from datetime import datetime, timedelta
from start import app
from patterns.repositories import IAuthRepository
from repositories import UserAuthRepository, UserAuthRepositoryProps
from models import User


@dataclass
class UserAuthServiceProps:
    email: str
    password: str


class UserAuthService:
    __minutes: float = 5

    def execute(self, args: UserAuthServiceProps) -> str:
        with app.databases.create_session() as session:
            user_auth_repository: IAuthRepository[
                UserAuthRepositoryProps, User
            ] = UserAuthRepository(session)

            user: User = user_auth_repository.auth(args)

            expired: float = (
                datetime.now() + timedelta(minutes=UserAuthService.__minutes)
            ).timestamp()

            payload: Mapping[str, Any] = {"user_uuid": user.id_uuid, "expired": expired}

            token: str = PyJWT().encode(payload, app.http.secret_key, "HS256")

            return token
