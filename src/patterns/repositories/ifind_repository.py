from typing import Protocol, Generic, TypeVar
from patterns.models import BaseModel

T = TypeVar("T")
TR = TypeVar("TR", None, BaseModel)


class IFindRepository(Protocol, Generic[T, TR]):
    def find(self, args: T) -> TR:
        pass
