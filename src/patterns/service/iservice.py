from typing import (
    Protocol,
    Generic,
    TypeVar,
    Any
)


T = TypeVar('T', Any, None)
TR = TypeVar('TR', Any, None)


class IService(Protocol, Generic[T, TR]):
    def execute(self, args: T) -> TR:
        pass