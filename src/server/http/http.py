from typing import Union
from flask import Flask, request, Request
from flask_restful import Api



class HTTP(Api):
    def __init__(
        self,
        host: str,
        port: Union[str, int],
        secret_key: str,
        debug: bool
    ):
        core: Flask = Flask(__name__)

        super().__init__(core)

        self.__core: Flask = core
        self.__host: str = host
        self.__port: Union[str, int] = port
        self.__secret_key: str = secret_key
        self.__debug: bool = debug
        self.__global_request: Request = request

    @property
    def core(self) -> Flask:
        return self.__core

    @property
    def host(self) -> str:
        return self.__host

    @property
    def secret_key(self) -> str:
        return self.__secret_key

    @property
    def global_request(self) -> Request:
        return self.__global_request

    def start(self) -> None:
        self.__core.run(
            host=self.__host,
            port=self.__port,
            debug=self.__debug
        )



