from start import app
from server.http import (
    HTTPController, 
    BaseResponse,
    ResponseSuccess
)


class DriveController(HTTPController):
    def post(self) -> BaseResponse:
        file_content: bytes = app.http.global_request.data

        with open('teste.txt', 'wb') as file:
            file.write(file_content)

        return ResponseSuccess()