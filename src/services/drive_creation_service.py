from dataclasses import dataclass
from start import app
from patterns.repositories import ICreateRepository, IFindRepository
from models import User
from repositories import (
    DriveCreateRepository,
    DriveCreateRepositoryProps,
    UserFindRepository,
    UserFindRepositoryProps,
)


@dataclass
class DriveCreateServiceProps:
    filename: str
    path: str
    user_uuid: str


@dataclass
class UserFindProps:
    user_uuid: str
    

@dataclass
class DriveCreateProps:
    path: str
    filename: str
    user: User
    

class DriveCreationService:
    def execute(self, args: DriveCreateServiceProps) -> None:
        with app.databases.create_session() as session:
            user_find_props: UserFindProps = UserFindProps(args.user_uuid)

            user_find_repository: IFindRepository[
                UserFindRepositoryProps, User
            ] = UserFindRepository(session)

            user: User = user_find_repository.find(user_find_props)

            drive_create_repository: ICreateRepository[
                DriveCreateRepositoryProps, None
            ] = DriveCreateRepository(session)

            drive_create_params: DriveCreateRepositoryProps = (
                DriveCreateProps(args.path, args.filename, user)
            )

            drive_create_repository.create(drive_create_params)

            session.commit()
