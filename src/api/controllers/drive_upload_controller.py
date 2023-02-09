from typing import Mapping, Any, BinaryIO
from base64 import b64encode

from start import app
from server.http import HTTPController, BaseResponse, ResponseSuccess
from patterns.service import IService
from services import DriveUploadService, DriveUploadServiceProps, DrivesUploadsService, DrivesUploadsServiceProps
from models import User
from api.middlewares import UserAuthMiddleware
from utils.constants import __MIME_TYPES__


userAuthMiddleware: UserAuthMiddleware = UserAuthMiddleware()


class DriveUploadController:
    class DriveUploadOne(HTTPController):
        @userAuthMiddleware.apply()
        def post(self, auth: User) -> BaseResponse:
            filename: str = app.http.global_request.headers['filename']

            filetype, = [
                type
                for type, mimetype in __MIME_TYPES__.items()
                if mimetype == app.http.global_request.headers['Content-Type']
            ]

            data: BinaryIO = app.http.global_request.stream

            drive_upload_props: DriveUploadServiceProps = DriveUploadServiceProps(
                user=auth,
                filename=f"{filename}.{filetype}",
                content=b64encode(data.read())
            )

            drive_upload_service: IService[
                DriveUploadServiceProps, None
            ] = DriveUploadService()

            drive_upload_service.execute(drive_upload_props)

            return ResponseSuccess()


    class DriveUploadMany(HTTPController):
        @userAuthMiddleware.apply()
        def post(self, auth: User) -> BaseResponse:
            data: Mapping[str, Any] = app.http.global_request.json

            drives_uploads_props: DrivesUploadsServiceProps = DrivesUploadsServiceProps(
                auth,
                **data
            )

            drives_uploads_service: IService[DrivesUploadsServiceProps, None] = DrivesUploadsService()

            drives_uploads_service.execute(drives_uploads_props)

            return ResponseSuccess()
