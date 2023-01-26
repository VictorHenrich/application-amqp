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
Target: TypeAlias = Callable[[Args, Kwargs], Union[BaseResponse, Response]]
Wrapper: TypeAlias = Callable[[Args, Kwargs], Any]
HandleReturn: TypeAlias = Union[
    Awaitable[Optional[Kwargs]], Optional[Kwargs], BaseResponse, Response
]


class HTTPMiddleware(ABC):
    @abstractmethod
    def handle(self, *args: Args, **kwargs: Kwargs) -> HandleReturn:
        pass

    def apply(self, *args: Args, **kwargs: Kwargs) -> Target:
        def wrapper(target: Target) -> Wrapper:
            def w(*a: Args, **k: Kwargs) -> Any:
                result: HandleReturn = self.handle(*args, **kwargs)

                if isinstance(result, Response):
                    return result

                else:
                    k_: Mapping[str, Any] = {**k, **(result or {})}

                    return target(*a, **k_)

            return w

        return wrapper
