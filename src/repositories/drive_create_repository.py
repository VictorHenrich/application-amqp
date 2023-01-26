from typing import Protocol
from patterns.repositories import BaseRepository
from models import User, Drive


class DriveCreateRepositoryParams(Protocol):
    path: str
    filename: str
    user: User


class DriveCreateRepository(BaseRepository):
    def create(self, args: DriveCreateRepositoryParams) -> None:
        drive: Drive = Drive()

        drive.id_user = args.user.id
        drive.name = args.filename
        drive.path = args.path

        self.session.add(drive)
