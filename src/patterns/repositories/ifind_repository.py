from typing import (
    Protocol,
    Generic,
    TypeVar
)


T = TypeVar('T')
TR = TypeVar('TR')


class IFindRepository(Protocol, Generic[T, TR]):
    def find(self, args: T) -> TR:
        pass