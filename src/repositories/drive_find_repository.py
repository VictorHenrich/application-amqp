from typing import Protocol
from patterns.repositories import BaseRepository
from models import Drive, User
from exceptions import DriveNotFoundError


class DriveFindRepositoryProps(Protocol):
    drive_uuid: str
    user_uuid: str


class DriveFindRepository(BaseRepository):
    def find(self, args: DriveFindRepositoryProps) -> Drive:
        drive: Drive = (
            self.session.query(Drive)
            .join(User, User.id == Drive.id_user)
            .filter(User.id_uuid == args.user_uuid, Drive.id_uuid == args.drive_uuid)
            .first()
        )

        if not drive:
            raise DriveNotFoundError()

        return drive
