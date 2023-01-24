from typing import (
    Protocol,
    Generic,
    TypeVar,
    Any
)

T = TypeVar('T')
TR = TypeVar('TR', None, Any)


class ICreateRepository(Protocol, Generic[T, TR]):
    def create(self, args: T) -> TR:
        pass