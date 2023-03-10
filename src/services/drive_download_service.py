from typing import Tuple, BinaryIO, Mapping, Any
from io import BytesIO
from dataclasses import dataclass
from pathlib import Path

from start import app
from patterns.repositories import IFindRepository

from consumers import AccessCreationConsumerPayload, EmailSendingConsumerPayload
from repositories import DriveFindRepository, DriveFindRepositoryProps
from models import User, Drive
from utils import FileUtil


@dataclass
class DriveDownloadServiceProps:
    user: User
    drive_uuid: str


@dataclass
class DriveFindProps:
    drive_uuid: str
    user_uuid: str


class DriveDownloadService:
    def execute(self, args: DriveDownloadServiceProps) -> Tuple[BinaryIO, str]:
        with app.databases.create_session() as session:
            drive_find_props: DriveFindRepositoryProps = DriveFindProps(
                args.drive_uuid, args.user.id_uuid
            )

            drive_find_repository: IFindRepository[
                DriveFindRepositoryProps, Drive
            ] = DriveFindRepository(session)

            drive: Drive = drive_find_repository.find(drive_find_props)

            full_path: Path = Path() / args.user.path / drive.path

            file: BytesIO = FileUtil.read(full_path, "rb")

            publisher_access_creation_payload: Mapping[
                str, Any
            ] = AccessCreationConsumerPayload(
                args.user.id_uuid, args.drive_uuid, "download"
            ).__dict__

            app.amqp.create_publisher(
                "publisher_access_creation",
                "exchange_access_creation",
                publisher_access_creation_payload,
            )

            publisher_email_seding_payload: Mapping[
                str, Any
            ] = EmailSendingConsumerPayload(
                (args.user.email,),
                "Acesso na plataforma DRIVE",
                f"Um download foi realizado com um usuário autenticado ({args.user.name.upper()}) "
                + f"\nRealizado download do arquivo {drive.name}",
            ).__dict__

            app.amqp.create_publisher(
                "publisher_email_sending",
                "exchange_email_sending",
                publisher_email_seding_payload,
            )

            return file, drive.name
