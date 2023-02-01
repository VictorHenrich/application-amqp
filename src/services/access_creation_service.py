from dataclasses import dataclass
from start import app
from patterns.repositories import ICreateRepository, IFindRepository
from repositories import (
    AccessCreateRepository,
    AccessCreateRepositoryProps,
    DriveFindRepository,
    DriveFindRepositoryProps,
    UserFindRepository,
    UserFindRepositoryProps,
)
from models import User, Drive


@dataclass
class AccessCreationServiceProps:
    user_uuid: str
    drive_uuid: str
    operation: str


@dataclass
class DriveFindProps:
    drive_uuid: str
    user_uuid: str


@dataclass
class UserFindProps:
    user_uuid: str


@dataclass
class AccessCreateProps:
    operation: str
    user: User
    drive: Drive


class AccessCreationService:
    def execute(self, args: AccessCreationServiceProps) -> None:
        with app.databases.create_session() as session:
            user_find_props: UserFindRepositoryProps = UserFindProps(args.user_uuid)

            user_find_repository: IFindRepository[
                UserFindRepositoryProps, User
            ] = UserFindRepository(session)

            user: User = user_find_repository.find(user_find_props)

            drive_find_props: DriveFindRepositoryProps = DriveFindProps(
                args.drive_uuid, user.id_uuid
            )

            drive_find_repository: IFindRepository[
                DriveFindRepositoryProps, Drive
            ] = DriveFindRepository(session)

            drive: Drive = drive_find_repository.find(drive_find_props)

            access_create_props: AccessCreateRepositoryProps = AccessCreateProps(
                args.operation, user, drive
            )

            access_create_repository: ICreateRepository[
                AccessCreateRepositoryProps, None
            ] = AccessCreateRepository(session)

            access_create_repository.create(access_create_props)

            session.commit()
