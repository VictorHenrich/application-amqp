from typing import Sequence, Mapping, Any, Union
from dataclasses import dataclass
from threading import Thread

from models import User
from patterns.service import IService
from services.drive_upload_service import DriveUploadService, DriveUploadServiceProps


@dataclass
class DrivesUploadsServiceProps:
    user: User
    drives: Sequence[Mapping[str, Any]]


class DrivesUploadsService:
    def __upload_file(
        self, user: User, filename: str, content: Union[str, bytes]
    ) -> None:
        drive_upload_props: DriveUploadServiceProps = DriveUploadServiceProps(
            filename, content, user
        )

        drive_upload_service: IService[
            DriveUploadServiceProps, None
        ] = DriveUploadService()

        drive_upload_service.execute(drive_upload_props)

    def execute(self, args: DrivesUploadsServiceProps) -> None:
        threads: Sequence[Thread] = [
            Thread(
                target=self.__upload_file,
                args=(args.user, drive["filename"], drive["content"]),
            )
            for drive in args.drives
        ]

        [thread.start() for thread in threads]
        [thread.join() for thread in threads]
