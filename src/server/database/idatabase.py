from typing import Protocol, Union, Mapping, Sequence, Any, TypeAlias
from sqlalchemy.orm import Session
from sqlalchemy.ext.asyncio import AsyncSession


Args: TypeAlias = Sequence[Any]
Kwargs: TypeAlias = Mapping[str, Any]


class IDatabase(Protocol):
    def create_session(
        self, *args: Args, **kwargs: Kwargs
    ) -> Union[Session, AsyncSession]:
        pass

    def migrate(self, drop_tables: bool, *args: Args, **kwargs: Kwargs) -> None:
        pass
