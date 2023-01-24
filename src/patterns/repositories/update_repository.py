from typing import (
    Protocol,
    Generic,
    TypeVar,
    Any
)


T = TypeVar('T')
TR = TypeVar('TR', None, Any)


class IUpdateRepository(Protocol, Generic[T, TR]):
    def update(self, args: T) -> TR:
        pass