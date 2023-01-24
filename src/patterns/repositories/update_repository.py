from typing import (
    Protocol,
    Generic,
    TypeVar
)
from patterns.models import BaseModel

T = TypeVar('T')
TR = TypeVar('TR', None, BaseModel)


class IUpdateRepository(Protocol, Generic[T, TR]):
    def update(self, args: T) -> TR:
        pass