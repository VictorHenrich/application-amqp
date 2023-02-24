from typing import Generic, Protocol, TypeVar


T = TypeVar("T", contravariant=True)
TR = TypeVar("TR", covariant=True)


class IAuthRepository(Protocol, Generic[T, TR]):
    def auth(self, args: T) -> TR:
        ...
