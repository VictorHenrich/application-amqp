from start import app
from server.http import HTTPController, BaseResponse


class TesteController(HTTPController):
    def get(self) -> BaseResponse:
        print(app.http.global_request.args)