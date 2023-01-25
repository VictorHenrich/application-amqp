from typing import BinaryIO
from dataclasses import dataclass
from pathlib import Path

from models import User, Drive


@dataclass
class DriveDownloadServiceProps:
    user: User
    drive: Drive


class DriveDownloadService:
    def execute(self, args: DriveDownloadServiceProps) -> BinaryIO:
        full_path: Path = Path() / args.user.path / args.drive.path

        return open(full_path, "rb")
