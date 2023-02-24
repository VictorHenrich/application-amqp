from typing import Protocol, Generic, TypeVar
from patterns.models import BaseModel

T = TypeVar("T", contravariant=True)
TR = TypeVar("TR", None, BaseModel, covariant=True)


class ICreateRepository(Protocol, Generic[T, TR]):
    def create(self, args: T) -> TR:
        ...
