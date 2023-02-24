from typing import Any, TypeAlias, Sequence, Mapping, Union
from abc import ABC
from flask_restful import Resource
from flask import Response

from .response import BaseResponse


Args: TypeAlias = Sequence[Any]
Kwargs: TypeAlias = Mapping[str, Any]


class HTTPController(Resource, ABC):
    def post(self, *args: Args, **kwargs: Kwargs) -> Union[BaseResponse, Response]:
        ...

    def put(self, *args: Args, **kwargs: Kwargs) -> Union[BaseResponse, Response]:
        ...

    def get(self, *args: Args, **kwargs: Kwargs) -> Union[BaseResponse, Response]:
        ...

    def delete(self, *args: Args, **kwargs: Kwargs) -> Union[BaseResponse, Response]:
        ...

    def patch(self, *args: Args, **kwargs: Kwargs) -> Union[BaseResponse, Response]:
        ...
