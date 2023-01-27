from typing import Union, Mapping, Any
from dataclasses import dataclass
from base64 import b64decode
from pathlib import Path

from start import app
from server.amqp import AMQPPublisher
from models import User
from utils.constants import __PATH_DRIVES__
from consumers import ConsumerDriveCreationPayload


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

        publisher_payload: Mapping[str, Any] = ConsumerDriveCreationPayload(
            args.filename, str(drive_path), args.user.id_uuid
        ).__dict__

        publisher: AMQPPublisher = AMQPPublisher(
            "publisher_drive_creation",
            app.amqp.default_connection,
            "exchange_drive_creation",
            publisher_payload,
        )

        publisher.start()
