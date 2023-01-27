from typing import Protocol
from patterns.repositories import BaseRepository
from models import User, Drive


class DriveCreateRepositoryProps(Protocol):
    path: str
    filename: str
    user: User


class DriveCreateRepository(BaseRepository):
    def create(self, args: DriveCreateRepositoryProps) -> None:
        drive: Drive = Drive()

        drive.id_user = args.user.id
        drive.name = args.filename
        drive.path = args.path

        self.session.add(drive)
