from start import app
from server.http import HTTPController, BaseResponse, ResponseSuccess


class DriveController(HTTPController):
    def post(self) -> BaseResponse:
        file_content: bytes = app.http.global_request.json

        print(list(app.http.global_request.headers.keys()))
