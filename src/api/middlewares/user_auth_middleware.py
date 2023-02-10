from start import app
from server.http import HTTPMiddleware, ResponseFailure
from patterns.service import IService
from models import User
from services import UserAuthTokenService, UserAuthTokenServiceProps
from exceptions import ExpiredTokenError, UserNotFoundError


class UserAuthMiddleware(HTTPMiddleware):
    def handle(self):
        authorization: str = app.http.global_request.headers.get("Authorization")

        if not authorization:
            return ResponseFailure("Authorization field was not reported in the header")

        user_auth_token_props: UserAuthTokenServiceProps = UserAuthTokenServiceProps(
            authorization
        )

        user_auth_token_service: IService[
            UserAuthTokenServiceProps, User
        ] = UserAuthTokenService()

        try:
            user: User = user_auth_token_service.execute(user_auth_token_props)

            return {"auth": user}

        except ExpiredTokenError as error:
            return ResponseFailure(str(error))

        except UserNotFoundError as error:
            return ResponseFailure(str(error))
