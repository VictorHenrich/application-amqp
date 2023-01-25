from dataclasses import dataclass
from start import app
from patterns.repositories import ICreateRepository
from models import User
from repositories import DriveCreateRepository, DriveCreateRepositoryParams


@dataclass
class DriveCreateServiceProps:
    filename: str
    content: bytes
    user: User


class DriveCreationService:
    def execute(self, args: DriveCreateServiceProps) -> None:
        with app.databases.create_session() as session:
            drive_create_repository: ICreateRepository[
                DriveCreateRepositoryParams, None
            ] = DriveCreateRepository(session)

            drive_create_params: DriveCreateRepositoryParams = (
                DriveCreateRepositoryParams(args.path, args.filename, args.user)
            )

            drive_create_repository.create(drive_create_params)

            session.commit()
