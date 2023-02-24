from typing import Protocol, Generic, TypeVar, Union
from patterns.models import BaseModel

T = TypeVar("T", contravariant=True)
TR = TypeVar("TR", bound=Union[None, BaseModel], covariant=True)


class IFindRepository(Protocol, Generic[T, TR]):
    def find(self, args: T) -> TR:
        ...
