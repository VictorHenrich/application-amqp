from typing import Protocol, Sequence
from patterns.repositories import BaseRepository
from models import Drive, User
from exceptions import DriveNotFoundError


class DriveFindManyRepositoryProps(Protocol):
    user_uuid: str


class DriveFindManyRepository(BaseRepository):
    def find(self, args: DriveFindManyRepositoryProps) -> Sequence[Drive]:
        drives: Sequence[Drive] = (
            self.session.query(Drive)
            .join(User, User.id == Drive.id_user)
            .filter(User.id_uuid == args.user_uuid)
            .all()
        )

        if not drives:
            raise DriveNotFoundError()

        return drives
