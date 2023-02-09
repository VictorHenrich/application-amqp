from typing import Sequence, Tuple, BinaryIO, Mapping, Any
from uuid import UUID

from start import app
from server.http import HTTPController, BaseResponse, ResponseIO
from patterns.service import IService
from services import DriveDownloadService, DriveDownloadServiceProps, DrivesDownloadService, DrivesDownloadServiceProps
from models import User
from api.middlewares import UserAuthMiddleware


userAuthMiddleware: UserAuthMiddleware = UserAuthMiddleware()


class DriveDownloadController:
    class DriveDownloadOne(HTTPController):
        @userAuthMiddleware.apply()
        def get(self, auth: User, drive_hash: UUID) -> BaseResponse:
            drive_download_props: DriveDownloadServiceProps = DriveDownloadServiceProps(
                auth, str(drive_hash)
            )

            drive_download_service: IService[
                DriveDownloadServiceProps, Tuple[BinaryIO, str]
            ] = DriveDownloadService()

            file, filename = drive_download_service.execute(drive_download_props)

            return ResponseIO(file, filename)

    class DriveDownloadMany(HTTPController):
        @userAuthMiddleware.apply()
        def post(self, auth: User) -> BaseResponse:
            data: Mapping[str, Any] = app.http.global_request.json

            drives_download_props: DrivesDownloadServiceProps = DrivesDownloadServiceProps(auth, data['drives'])

            drives_download_service: IService[DrivesDownloadServiceProps, Sequence[bytes]] = DrivesDownloadService()

            zip_file: Sequence[bytes] = drives_download_service.execute(drives_download_props)

            return ResponseIO(zip_file, 'arquivo.zip')
