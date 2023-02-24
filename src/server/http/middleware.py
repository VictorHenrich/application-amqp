from abc import ABC, abstractmethod
from typing import (
    TypeAlias,
    Mapping,
    Sequence,
    Callable,
    Any,
    Union,
    Optional,
    Awaitable,
)
from flask import Response
from .response import BaseResponse

Args: TypeAlias = Sequence[Any]
Kwargs: TypeAlias = Mapping[str, Any]
Target: TypeAlias = Callable[[Any], Union[BaseResponse, Response]]
Wrapper: TypeAlias = Callable[[Any], Union[BaseResponse, Response]]
Decorator: TypeAlias = Callable[[Target], Wrapper]
HandleReturn: TypeAlias = Union[
    Awaitable[Optional[Kwargs]], Optional[Kwargs], BaseResponse, Response
]


class HTTPMiddleware(ABC):
    @abstractmethod
    def handle(self, *args: Args, **kwargs: Kwargs) -> HandleReturn:
        ...

    def apply(self, *args: Args, **kwargs: Kwargs) -> Decorator:
        def decorator(target: Target) -> Wrapper:
            def wrapper(*a: Args, **k: Kwargs) -> Union[BaseResponse, Response]:
                result: HandleReturn = self.handle(*args, **kwargs)

                if isinstance(result, Response):
                    return result

                if isinstance(result, dict):
                    k_: Mapping[str, Any] = {**k, **(result or {})}

                    return target(*a, **k_)

                else:
                    raise Exception(
                        "Response returned by request is invalid Response | BaseResponse"
                    )

            return wrapper

        return decorator
