from typing import Union
from dataclasses import dataclass
from base64 import b64decode
from pathlib import Path
from pika import ConnectionParameters
from server.amqp import AMQPPublisher, ConnectionBuilder
from models import User
from utils.constants import __PATH_DRIVES__
from consumers import PayloadDriveCreation


@dataclass
class DriveUploadServiceProps:
    filename: str
    content: Union[str, bytes]
    user: User


class DriveUploadService:
    def execute(self, args: DriveUploadServiceProps) -> None:
        drive_path: Path = Path(__PATH_DRIVES__) / args.user.path / args.filename

        drive_content: bytes = b64decode(args.content)

        with open(drive_path, "wb") as file:
            file.write(drive_content)

        connection: ConnectionParameters = (
            ConnectionBuilder()
            .set_host("localhost")
            .set_port(5672)
            .set_credentials("guest", "guest")
            .build()
        )

        publisher: AMQPPublisher = AMQPPublisher(
            "publisher_drive_creation",
            connection,
            "exchange_drive_creation",
            PayloadDriveCreation(args.filename, drive_path, args.user.id_uuid),
        )

        publisher.start()
