from typing import Protocol, Generic, TypeVar
from patterns.models import BaseModel

T = TypeVar("T", contravariant=True)
TR = TypeVar("TR", None, BaseModel, covariant=True)


class IDeleteRepository(Protocol, Generic[T, TR]):
    def delete(self, args: T) -> TR:
        ...
