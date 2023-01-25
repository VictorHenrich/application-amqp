from dataclasses import dataclass
from patterns.repositories import BaseRepository, ICreateRepository
from models import User, Drive


@dataclass
class DriveCreateRepositoryParams:
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
