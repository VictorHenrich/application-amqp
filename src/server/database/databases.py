from typing import Dict, Union, Sequence, Any, Optional
from sqlalchemy.orm import Session
from sqlalchemy.ext.asyncio import AsyncSession

from .idatabase import IDatabase
from .database import Database
from server.database import idatabase


class Databases:
    def __init__(self) -> None:
        self.__bases: Dict[str, IDatabase] = {}

    def get_database(self, name: Optional[str] = None) -> IDatabase:
        try:
            if len(self.__bases) == 1 or not name:
                return list(self.__bases.values())[0]

            else:
                return [
                    b
                    for base_name, b in self.__bases.items()
                    if base_name.upper() == name.upper()
                ][0]

        except IndexError:
            raise Exception("Database not found!")

    def add_base(self, database: Database) -> None:
        self.__bases[f"{database.name}"] = database

    def create_session(
        self,
        database_name: Optional[str] = None,
        *args: Sequence[Any],
        **kwargs: Dict[str, Any],
    ) -> Union[Session, AsyncSession]:
        database: IDatabase = self.get_database(database_name)

        return database.create_session(*args, **kwargs)

    def migrate(
        self, database_name: Optional[str] = None, drop_tables: bool = False
    ) -> None:
        database: IDatabase = self.get_database(database_name)

        database.migrate(drop_tables)
