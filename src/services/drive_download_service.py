from typing import Mapping, Any, Sequence
from dataclasses import dataclass
from pathlib import Path

from start import app
from server.amqp import AMQPPublisher
from patterns.repositories import IFindRepository
from consumers import ConsumerAccessCreationPayload
from repositories import DriveFindRepository, DriveFindRepositoryProps
from models import User, Drive


@dataclass
class DriveDownloadServiceProps:
    user: User
    drive_uuid: str


@dataclass
class DriveFindProps:
    drive_uuid: str
    user_uuid: str


class DriveDownloadService:
    def execute(self, args: DriveDownloadServiceProps) -> Sequence[bytes]:
        with app.databases.create_session() as session:
            drive_find_props: DriveFindRepositoryProps = DriveFindProps(
                args.drive_uuid, args.user.id_uuid
            )

            drive_find_repository: IFindRepository[
                DriveFindRepositoryProps, Drive
            ] = DriveFindRepository(session)

            drive: Drive = drive_find_repository.find(drive_find_props)

            full_path: Path = Path() / args.user.path / drive.path

            with open(full_path, "rb") as file:
                publisher_payload: Mapping[str, Any] = ConsumerAccessCreationPayload(
                    args.user.id_uuid, args.drive_uuid, "download"
                ).__dict__

                publisher: AMQPPublisher = AMQPPublisher(
                    "publisher_access_creation",
                    app.amqp.default_connection,
                    "exchange_access_creation",
                    publisher_payload,
                )

                publisher.start()

                return file.readlines()
