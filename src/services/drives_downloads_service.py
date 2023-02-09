from typing import Sequence, BinaryIO, Tuple, IO
from dataclasses import dataclass
from queue import Queue
from threading import Thread

from patterns.service import IService
from models import User
from utils import FileUtil
from .drive_download_service import DriveDownloadService, DriveDownloadServiceProps


@dataclass
class DrivesDownloadServiceProps:
    user: User
    drives_uuids: Sequence[str]


@dataclass
class DriveFindProps:
    drive_uuid: str
    user_uuid: str


class DrivesDownloadService:
    def __download_drive(self, drive_uuid: str, user: User, queue: Queue) -> BinaryIO:
        drive_download_props: DriveDownloadServiceProps = DriveDownloadServiceProps(
            user, drive_uuid
        )

        drive_download_service: IService[
            DriveDownloadServiceProps, Tuple[BinaryIO, str]
        ] = DriveDownloadService()

        file, _ = drive_download_service.execute(drive_download_props)

        queue.put(file)

    def execute(self, args: DrivesDownloadServiceProps) -> Sequence[bytes]:
        q: Queue = Queue()

        threads: Sequence[Thread] = [
            Thread(target=self.__download_drive, args=(drive_uuid, args.user, q))
            for drive_uuid in args.drives_uuids
        ]

        [thread.start() for thread in threads]

        [thread.join() for thread in threads]

        files: Sequence[BinaryIO] = list(q.queue)

        file_zip: IO = FileUtil.zip(files, "file_teste.zip")

        return file_zip.readlines()
