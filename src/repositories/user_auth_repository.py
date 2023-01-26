from typing import Protocol
from patterns.repositories import BaseRepository
from exceptions import UserNotFoundError
from models import User


class UserAuthRepositoryProps(Protocol):
    email: str
    password: str


class UserAuthRepository(BaseRepository):
    def auth(self, args: UserAuthRepositoryProps) -> User:
        user: User = (
            self.session.query(User)
            .filter(
                User.email == args.email,
                User.password == args.password,
            )
            .first()
        )

        if not user:
            raise UserNotFoundError()

        return user
