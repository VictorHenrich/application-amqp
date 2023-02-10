from typing import Protocol, Sequence

from dataclasses import dataclass
from patterns.repositories import BaseRepository, IFindRepository
from repositories import DriveFindManyRepository, DriveFindManyRepositoryProps
from models import User, Drive


class UserDeleteRepositoryProps(Protocol):
    user: User


@dataclass
class DriveFindProps:
    user_uuid: str


class UserDeleteRepository(BaseRepository):
    def delete(self, args: UserDeleteRepositoryProps) -> None:
        drive_find_props: DriveFindManyRepositoryProps = DriveFindProps(
            args.user.id_uuid
        )

        drive_find_many_repository: IFindRepository[
            DriveFindManyRepositoryProps, Sequence[Drive]
        ] = DriveFindManyRepository(self.session)

        drives: Sequence[Drive] = drive_find_many_repository.find(drive_find_props)

        for drive in drives:
            self.session.delete(drive)

        self.session.delete(args.user)
