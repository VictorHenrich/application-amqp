from typing import Protocol
from patterns.repositories import BaseRepository
from exceptions import UserNotFoundError
from models import User


class UserFindRepositoryProps(Protocol):
    user_uuid: str


class UserFindRepository(BaseRepository):
    def find(self, args: UserFindRepositoryProps) -> User:
        user: User = (
            self.session.query(User).filter(User.id_uuid == args.user_uuid).first()
        )

        if not user:
            raise UserNotFoundError()

        return user
