from typing import Union, Mapping, Any
from dataclasses import dataclass
from base64 import b64decode
from pathlib import Path

from start import app
from models import User
from utils.constants import __PATH_DRIVES__
from utils import FileUtil
import consumers


@dataclass
class DriveUploadServiceProps:
    filename: str
    content: Union[str, bytes]
    user: User


class DriveUploadService:
    def execute(self, args: DriveUploadServiceProps) -> None:
        drive_path: Path = Path(__PATH_DRIVES__) / args.user.path / args.filename

        drive_content: bytes = b64decode(args.content)

        FileUtil.write(drive_path, drive_content, "wb")

        publisher_payload: Mapping[str, Any] = consumers.DriveCreationConsumerPayload(
            args.filename, str(drive_path), args.user.id_uuid
        ).__dict__

        app.amqp.create_publisher(
            "publisher_drive_creation", "exchange_drive_creation", publisher_payload
        )
