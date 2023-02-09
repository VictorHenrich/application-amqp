from typing import Protocol

from patterns.repositories import BaseRepository
from models import User


class UserDeleteRepositoryProps(Protocol):
    user: User


class UserDeleteRepository(BaseRepository):
    def update(self, args: UserDeleteRepositoryProps) -> None:
        self.session.delete(args.user)
