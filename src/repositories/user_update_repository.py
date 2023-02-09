from typing import Protocol

from patterns.repositories import BaseRepository
from models import User


class UserUpdateRepositoryProps(Protocol):
    name: str
    email: str
    password: str
    user: User


class UserUpdateRepository(BaseRepository):
    def update(self, args: UserUpdateRepositoryProps) -> None:
        args.user.name = args.name
        args.user.email = args.email
        args.user.password = args.password

        self.session.add(args.user)
