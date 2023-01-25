from typing import Generic, Protocol, TypeVar


T = TypeVar("T")
TR = TypeVar("TR")


class IAuthRepository(Protocol, Generic[T, TR]):
    def auth(self, args: T) -> TR:
        pass
