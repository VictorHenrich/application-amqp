from __future__ import annotations
from typing import (
    Optional,
    Union,
    TypeAlias
)
from dataclasses import dataclass

from .database import Database


OptionalString: TypeAlias = Optional[str]
StringOrNumber: TypeAlias = Union[str, int]
OptionalStringOrNamber: TypeAlias = Optional[StringOrNumber]


@dataclass
class DatabaseBuilder:
    name: str
    host: OptionalString = None
    port: OptionalStringOrNamber = None
    dbname: OptionalString = None
    username: OptionalString = None
    password: OptionalString = None
    dialect: OptionalString = None
    drive_default: OptionalString = None
    drive_async: OptionalString = None
    async_: bool = False
    debug: bool = False

    def set_host(self, host: str) -> DatabaseBuilder:
        self.host = host

        return self

    def set_port(self, port: StringOrNumber) -> DatabaseBuilder:
        self.port = port

        return self

    def set_dbname(self, dbname: str) -> DatabaseBuilder:
        self.dbname = dbname

        return self

    def set_credentials(self, username: str, password: str) -> DatabaseBuilder:
        self.username = username
        self.password = password

        return self

    def set_dialect(self, dialect: str) -> DatabaseBuilder:
        self.dialect = dialect
        
        return self

    def set_drives(self, drive_default: OptionalString = None, drive_async: OptionalString = None) -> DatabaseBuilder:
        self.drive_default = drive_default
        self.drive_async = drive_async

        return self

    def set_debug(self, debug: bool) -> DatabaseBuilder:
        self.debug = debug

        return self

    def set_async(self, async_: bool) -> DatabaseBuilder:
        self.async_ = async_

        return self

    def build(self) -> Database:
        drive: str = self.drive_async if self.async_ else self.drive_default

        connection_url: str = f"{self.dialect}+{drive}://{self.username}:{self.password}@{self.host}:{self.port}/{self.dbname}"

        return Database(
            connection_url,
            self.name,
            self.debug,
            self.async_
        )