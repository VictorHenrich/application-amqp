from typing import (
    Protocol,
    TypeAlias,
    Mapping,
    Sequence,
    Any,
    Generic,
    TypeVar,
    Optional,
)


Args: TypeAlias = Sequence[Any]
Kwargs: TypeAlias = Mapping[str, Any]

T = TypeVar("T", contravariant=True)


class ICommand(Protocol, Generic[T]):
    def execute(self, args: T) -> None:
        ...
