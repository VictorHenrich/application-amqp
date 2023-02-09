from dataclasses import dataclass

from start import app
from models import User
from patterns.repositories import IUpdateRepository
from repositories import UserUpdateRepository, UserUpdateRepositoryProps


@dataclass
class UserUpdateServiceProps:
    name: str
    email: str
    password: str
    user: User


class UserUpdateService:
    def execute(self, args: UserUpdateServiceProps) -> None:
        with app.databases.create_session() as session:
            user_update_repository: IUpdateRepository[
                UserUpdateRepositoryProps, None
            ] = UserUpdateRepository(session)

            user_update_repository.update(args)
