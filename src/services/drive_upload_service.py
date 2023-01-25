from dataclasses import dataclass
from base64 import b64decode
from typing import BinaryIO
from pathlib import Path

from models import User
from utils.constants import __PATH_DRIVES__


@dataclass
class DriveUploadServiceProps:
    filename: str
    content: str | BinaryIO
    user: User


class DriveUploadService:
    def execute(self, args: DriveUploadServiceProps) -> None:
        drive_path: Path = Path(__PATH_DRIVES__) / args.user.path / args.filename

        drive_content: bytes = b64decode(args.content)

        with open(drive_path, "wb") as file:
            file.write(drive_content)
