from typing import Protocol, Generic, TypeVar, Union
from patterns.models import BaseModel

T = TypeVar("T")
TR = TypeVar("TR", bound=Union[None, BaseModel])


class IFindRepository(Protocol, Generic[T, TR]):
    def find(self, args: T) -> TR:
        pass
