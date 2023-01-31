from typing import Sequence, Tuple
from uuid import UUID

from server.http import HTTPController, BaseResponse, ResponseIO
from patterns.service import IService
from services import DriveDownloadService, DriveDownloadServiceProps
from models import User
from api.middlewares import UserAuthMiddleware


userAuthMiddleware: UserAuthMiddleware = UserAuthMiddleware()


class DriveDownloadController(HTTPController):
    @userAuthMiddleware.apply()
    def get(self, auth: User, drive_hash: UUID) -> BaseResponse:
        drive_download_props: DriveDownloadServiceProps = DriveDownloadServiceProps(
            auth,
            str(drive_hash)
        )

        drive_download_service: IService[DriveDownloadServiceProps, Tuple[Sequence[bytes], str]] = DriveDownloadService()

        file, filename = drive_download_service.execute(drive_download_props)

        return ResponseIO(file, filename)



