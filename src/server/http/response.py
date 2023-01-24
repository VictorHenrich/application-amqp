from abc import ABC
import json
from typing import Optional, Any, Mapping, TypeAlias
from flask import Response


MappingDict: TypeAlias = Mapping[str, Any]


class BaseResponse(Response, ABC):
    def __init__(
        self,
        message: str,
        status: int,
        data: Any,
        headers: MappingDict = None
    ) -> None:
        response_json: MappingDict = {
            "message": message,
            "status": status
        }

        headers_: MappingDict = {
            "Content-Type": "application/json",
            **(headers or {})
        }

        if data is not None:
            response_json['result'] = data

        super().__init__(
            response=json.dumps(response_json),
            headers=headers_,
            status=status
        )


class ResponseSuccess(BaseResponse):
    def __init__(
        self, 
        data: Optional[Any] = None,
        message: str = "OK", 
        status: int = 200,  
        headers: MappingDict = None
    ) -> None:
        super().__init__(message, status, data, headers)


class ResponseFailure(BaseResponse):
    def __init__(
        self, 
        data: Any,
        message: str = "ERROR", 
        status: int = 500,  
        headers: MappingDict = None
    ) -> None:
        super().__init__(message, status, data, headers)


class ResponseNotFound(BaseResponse):
    def __init__(
        self, 
        data: Any,
        message: str = "NOT FOUND", 
        status: int = 404,  
        headers: MappingDict = None
    ) -> None:
        super().__init__(message, status, data, headers)


class ResponseUnauthorized(BaseResponse):
    def __init__(
        self, 
        data: Any,
        message: str = "UNAUTHORIZED", 
        status: int = 401,  
        headers: MappingDict = None
    ) -> None:
        super().__init__(message, status, data, headers)


class ResponseIO(Response):
    pass
        