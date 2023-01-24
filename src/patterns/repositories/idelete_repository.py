from typing import (
    Protocol,
    Generic,
    TypeVar,
    Any
)


T = TypeVar('T')
TR = TypeVar('TR', None, Any)


class IDeleteRepository(Protocol, Generic[T, TR]):
    def delete(self, args: T) -> TR:
        pass