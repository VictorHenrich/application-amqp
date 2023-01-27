from typing import Protocol, TypeAlias, TypeVar
from patterns.repositories import BaseRepository
from models import User, Drive, Access


class AccessCreateRepositoryProps(Protocol):
    operation: str
    user: User
    drive: Drive


class AccessCreateRepository(BaseRepository):
    def create(self, args: AccessCreateRepositoryProps) -> None:
        access: Access = Access()

        access.operation = args.operation
        access.id_drive = args.drive.id
        access.id_user = args.user.id

        self.session.add(access)
