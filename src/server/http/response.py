from abc import ABC
import json
from io import IOBase
from typing import Optional, Any, Mapping, TypeAlias, Union, IO, Sequence, Union
from flask import Response
from utils.constants import __MIME_TYPES__


MappingDict: TypeAlias = Mapping[str, Any]
ContentFile: TypeAlias = Union[str, bytes, IO]
StreamFile: TypeAlias = Sequence[Union[bytes, str]]


class BaseResponse(Response, ABC):
    def __init__(
        self, message: str, status: int, data: Any, headers: MappingDict = None
    ) -> None:
        response_json: MappingDict = {"message": message, "status": status}

        headers_: MappingDict = {"Content-Type": "application/json", **(headers or {})}

        if data is not None:
            response_json["result"] = data

        super().__init__(
            response=json.dumps(response_json), headers=headers_, status=status
        )


class ResponseSuccess(BaseResponse):
    def __init__(
        self,
        data: Optional[Any] = None,
        message: str = "OK",
        status: int = 200,
        headers: MappingDict = None,
    ) -> None:
        super().__init__(message, status, data, headers)


class ResponseFailure(BaseResponse):
    def __init__(
        self,
        data: Any,
        message: str = "ERROR",
        status: int = 500,
        headers: MappingDict = None,
    ) -> None:
        super().__init__(message, status, data, headers)


class ResponseNotFound(BaseResponse):
    def __init__(
        self,
        data: Any,
        message: str = "NOT FOUND",
        status: int = 404,
        headers: MappingDict = None,
    ) -> None:
        super().__init__(message, status, data, headers)


class ResponseUnauthorized(BaseResponse):
    def __init__(
        self,
        data: Any,
        message: str = "UNAUTHORIZED",
        status: int = 401,
        headers: MappingDict = None,
    ) -> None:
        super().__init__(message, status, data, headers)


class ResponseIO(Response):
    def __init__(
        self,
        content: ContentFile,
        filename: str,
        status=200,
        headers: MappingDict = None,
    ) -> None:
        response: StreamFile = self.__handle_content(content)

        mimetype: str = self.__get_mimetype(filename)

        headers_: Mapping[str, Any] = {
            "Content-Type": mimetype,
            "Content-Disposition": f"attachment; filename='{filename}'",
            **(headers or {}),
        }

        super().__init__(response, status, headers_)

    def __get_mimetype(self, filename: str) -> str:
        _, filetype = filename.split(".")

        try:
            return __MIME_TYPES__[filetype]

        except KeyError:
            return __MIME_TYPES__["bin"]

    def __handle_content(self, content: ContentFile) -> StreamFile:
        if isinstance(content, IOBase):
            return self.__handle_content_io(content)

        if isinstance(content, (str, bytes, Sequence)):
            return self.__handle_content_default(content)

        else:
            raise Exception("Invalid content type")

    def __handle_content_io(self, content: IO) -> StreamFile:
        if not content.readable():
            raise Exception("IO content needs to be readable")

        return content.readlines()

    def __handle_content_default(self, content: Union[str, bytes]) -> StreamFile:
        if type(content) is str:
            return content.split()

        if type(content) is bytes:
            return content.split()

        if isinstance(content, Sequence):
            return content
