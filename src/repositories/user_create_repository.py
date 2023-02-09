from typing import Protocol

from patterns.repositories import BaseRepository
from models import User


class UserCreateRepositoryProps(Protocol):
    name: str
    email: str
    password: str
    path: str


class UserCreateRepository(BaseRepository):
    def create(self, args: UserCreateRepositoryProps) -> None:
        user: User = User()

        user.name = args.name
        user.email = args.email
        user.password = args.password
        user.path = args.path

        self.session.add(user)
