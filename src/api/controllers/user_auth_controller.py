from typing import Mapping, Any
from start import app
from server.http import HTTPController, BaseResponse, ResponseSuccess, ResponseFailure
from services import UserAuthService, UserAuthServiceProps
from patterns.service import IService
from exceptions import UserNotFoundError


class UserAuthController(HTTPController):
    def post(self) -> BaseResponse:
        data: Mapping[str, Any] = app.http.global_request.json

        user_auth_service_props: UserAuthServiceProps = UserAuthServiceProps(**data)

        user_auth_service: IService[UserAuthServiceProps, str] = UserAuthService()

        try:

            token: str = user_auth_service.execute(user_auth_service_props)

            return ResponseSuccess(token)

        except UserNotFoundError as error:
            return ResponseFailure(data=str(error))
