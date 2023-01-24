from typing import (
    Union, 
    Mapping, 
    Any,
    Sequence,
    Coroutine,
    Awaitable
)
from sqlalchemy.engine import create_engine, Engine
from sqlalchemy.orm.session import Session, sessionmaker
from sqlalchemy.ext.asyncio import create_async_engine, AsyncEngine, AsyncSession
from sqlalchemy.orm.decl_api import declarative_base, DeclarativeMeta
import asyncio


class Database:
    def __init__(
        self,
        connection_url: str,
        name: str,
        debug: bool,
        async_: bool
    ) -> None:
        self.__engine: Union[Engine, AsyncEngine] = self.__create_engine(
            connection_url,
            debug,
            async_
        )

        self.__Model: type[DeclarativeMeta] = declarative_base(self.__engine)

        self.__name: str = name

    @property
    def Model(self) -> type[DeclarativeMeta]:
        return self.__Model

    @property
    def engine(self) -> Union[Engine, AsyncEngine]:
        return self.__engine

    def name(self) -> str:
        return self.__name

    def create_session(self, *args: Sequence[Any], **kwargs: Mapping[str, Any]) -> Union[Session, AsyncSession]:
        return sessionmaker(
            self.__engine,
            AsyncSession if type(self.__engine) is AsyncEngine else Session,
            *args,
            **kwargs
        )()

    def migrate(self, drop_tables: bool = False):
        if type(self.__engine) is AsyncEngine:
            asyncio.run(self.__migrate_async(drop_tables))

        else:
            self.__migrate_default(drop_tables)

        print(f'{self.__name.upper()} DATABASE MIGRATED SUCCESSFULLY!')

    def __migrate_default(self, drop_tables: bool) -> None:
        if drop_tables:
            self.__Model.metadata.drop_all(self.__engine)

        self.__Model.metadata.create_all(self.__engine)

    async def __migrate_async(self, drop_tables: bool) -> Awaitable[None]:
        async with self.__engine.begin() as connection:
            if drop_tables:
                await connection.run_sync(self.__Model.metadata.drop_all)

            await connection.run_sync(self.__Model.metadata.create_all)

    def __create_engine(self, connection_url: str, debug: bool, async_: bool) -> Union[Engine, AsyncEngine]:
        creation_params: Mapping[str, Any] = {
            "url": connection_url,
            "echo": debug
        }

        if not async_:
            return create_engine(**creation_params)

        else:
            return create_async_engine(**creation_params)
