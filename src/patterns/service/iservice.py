from typing import Protocol, Generic, TypeVar, Any


T = TypeVar("T", Any, None, contravariant=True)
TR = TypeVar("TR", Any, None, covariant=True)


class IService(Protocol, Generic[T, TR]):
    def execute(self, args: T) -> TR:
        ...
