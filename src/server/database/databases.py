from typing import Mapping, Union, Sequence, Any, Optional
from sqlalchemy.orm import Session
from sqlalchemy.ext.asyncio import AsyncSession

from .idatabase import IDatabase
from .database import Database



class Databases:
    def __init__(
        self
    ) -> None:
        self.__bases: Mapping[str, IDatabase] = {}

    def get_database(self, name: Optional[str]) -> Database:
        try:
            if len(self.__bases) == 1 or not name:
                list(self.__bases.values())[0]

            else:
                return [
                    b
                    for base_name, b in self.__bases.items()
                    if base_name.upper() == name.upper()
                ][0]

        except IndexError:
            raise Exception('Database not found!')


    def add_base(self, database: Database) -> None:
        self.__bases[database.name] = database

    def create_session(self, database_name: Optional[str], *args: Sequence[Any], **kwargs: Mapping[str, Any]) -> Union[Session, AsyncSession]:
        database: Database = self.get_database(database_name)

        return database.create_session(*args, **kwargs)

    def migrate(self, database_name: Optional[str], drop_tables: bool) -> None:
        database: Database = self.get_database(database_name)

        database.migrate(drop_tables)

