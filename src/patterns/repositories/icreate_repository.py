from typing import (
    Protocol,
    Generic,
    TypeVar
)
from patterns.models import BaseModel

T = TypeVar('T')
TR = TypeVar('TR', None, BaseModel)


class ICreateRepository(Protocol, Generic[T, TR]):
    def create(self, args: T) -> TR:
        pass