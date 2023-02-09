from typing import Mapping, Any

from start import app
from server.http import HTTPController, HTTPMiddleware, BaseResponse, ResponseSuccess
from patterns.service import IService
from api.middlewares import UserAuthMiddleware
from models import User
from services import (
    UserCreationService,
    UserCreationServiceProps,
    UserUpdateService,
    UserUpdateServiceProps,
    UserExclusionService,
    UserExclusionServiceProps,
)

user_auth_middleware: HTTPMiddleware = UserAuthMiddleware()


class UserController(HTTPController):
    @user_auth_middleware.apply()
    def get(self, auth: User) -> BaseResponse:
        response_json: Mapping[str, Any] = {
            "name": auth.name,
            "email": auth.email,
            "uuid": auth.id_uuid,
        }

        return ResponseSuccess(response_json)

    def post(self) -> BaseResponse:
        data: Mapping[str, Any] = app.http.global_request.json

        user_creation_props: UserCreationServiceProps = UserCreationServiceProps(**data)

        user_creation_service: IService[
            UserCreationServiceProps, None
        ] = UserCreationService()

        user_creation_service.execute(user_creation_props)

        return ResponseSuccess()

    @user_auth_middleware.apply()
    def put(self, auth: User):
        data: Mapping[str, Any] = app.http.global_request.json

        user_update_props: UserUpdateServiceProps = UserUpdateServiceProps(
            **data, user=auth
        )

        user_update_service: IService[
            UserUpdateServiceProps, None
        ] = UserUpdateService()

        user_update_service.execute(user_update_props)

        return ResponseSuccess()

    @user_auth_middleware.apply()
    def delete(self, auth: User):
        user_exclusion_props: UserExclusionServiceProps = UserExclusionServiceProps(
            auth
        )

        user_exclusion_service: IService[
            UserExclusionServiceProps, None
        ] = UserExclusionService()

        user_exclusion_service.execute(user_exclusion_props)

        return ResponseSuccess()
