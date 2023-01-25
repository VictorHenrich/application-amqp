from typing import Protocol, Generic, TypeVar
from patterns.models import BaseModel

T = TypeVar("T")
TR = TypeVar("TR", None, BaseModel)


class IDeleteRepository(Protocol, Generic[T, TR]):
    def delete(self, args: T) -> TR:
        pass
