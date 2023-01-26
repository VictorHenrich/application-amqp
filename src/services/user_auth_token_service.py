from typing import Mapping, Any
from dataclasses import dataclass
from datetime import datetime
from jwt import PyJWT
from start import app
from patterns.repositories import IFindRepository
from exceptions import ExpiredTokenError
from repositories import UserFindRepositoryProps, UserFindRepository
from models import User


@dataclass
class UserAuthTokenServiceProps:
    token: str


@dataclass
class UserFindProps:
    user_uuid: str


class UserAuthTokenService:
    def execute(self, args: UserAuthTokenServiceProps) -> User:
        with app.databases.create_session() as session:
            payload: Mapping[str, Any] = PyJWT().decode(
                args.token, app.http.secret_key, ["HS256"]
            )

            if payload["expired"] <= datetime.now().timestamp():
                raise ExpiredTokenError()

            user_find_repository: IFindRepository[
                UserFindRepositoryProps, User
            ] = UserFindRepository(session)

            user_find_props: UserFindProps = UserFindProps(payload["user_uuid"])

            user: User = user_find_repository.find(user_find_props)

            return user
