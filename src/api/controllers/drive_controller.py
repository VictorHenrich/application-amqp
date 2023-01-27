from typing import Mapping, Any
from start import app
from server.http import HTTPController, BaseResponse, ResponseSuccess
from patterns.service import IService
from services import DriveUploadService, DriveUploadServiceProps
from models import User
from api.middlewares import UserAuthMiddleware


userAuthMiddleware: UserAuthMiddleware = UserAuthMiddleware()


class DriveController(HTTPController):
    @userAuthMiddleware.apply()
    def post(self, auth: User) -> BaseResponse:
        data: Mapping[str, Any] = app.http.global_request.json

        drive_upload_props: DriveUploadServiceProps = DriveUploadServiceProps(
            **data, user=auth
        )

        drive_upload_service: IService[
            DriveUploadServiceProps, None
        ] = DriveUploadService()

        drive_upload_service.execute(drive_upload_props)

        return ResponseSuccess()

    @userAuthMiddleware.apply()
    def get(self, auth: User) -> BaseResponse:
        pass
