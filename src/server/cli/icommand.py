from typing import (
    Protocol, 
    TypeAlias, 
    Mapping, 
    Sequence, 
    Any,
    Generic,
    TypeVar
)


Args: TypeAlias = Sequence[Any]
Kwargs: TypeAlias = Mapping[str, Any]

T = TypeVar('T')

class ICommand(Protocol, Generic[T]):
    def execute(self, args: T) -> None:
        pass