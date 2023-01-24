from dataclasses import dataclass
from typing import (
    Union, 
    Mapping, 
    Any, 
    Sequence, 
    TypeAlias,
    Callable,
)

from .http import HTTP
from .cli import ControllerTaskManagers
from .database import Databases, DatabaseBuilder, Database
from .amqp import AMQP


MappingDict: TypeAlias = Mapping[str, Any]
FunctionListener: TypeAlias = Callable[[None], None]


@dataclass
class Server:
    def __init__(
        self,
        http: HTTP,
        cli: ControllerTaskManagers,
        databases: Databases,
        amqp: AMQP
    ) -> None:
        self.__http: HTTP = http
        self.__cli: ControllerTaskManagers = cli
        self.__databases: Databases = databases
        self.__amqp: AMQP = amqp
    
    @property
    def http(self) -> HTTP:
        return self.__http

    @property
    def cli(self) -> ControllerTaskManagers:
        return self.__cli

    @property
    def databases(self) -> Databases:
        return self.__databases

    @property
    def amqp(self) -> AMQP:
        return self.__amqp

    def start(self) -> None:
        import tasks

        self.__cli.execute()



class ServerFactory:
    @staticmethod
    def __create_http(
        host: str,
        port: Union[str, int],
        secret_key: str,
        debug: bool = True
    ) -> HTTP:
        return HTTP(
            host,
            port,
            secret_key,
            debug
        )

    @staticmethod
    def __create_cli(
        name: str,
        managers: Sequence[str],
        version: Union[float, str] = 1, 
        description: str = "",
        usage: str = ""
    ) -> ControllerTaskManagers:

        cli: ControllerTaskManagers = ControllerTaskManagers(
            name,
            version,
            description,
            usage
        )

        for manager_name in managers:
            cli.create_task_manager(manager_name)

        return cli

    @staticmethod
    def __create_databases(
        bases: Mapping[str, MappingDict] = []
    ) -> Databases:
        databases: Databases = Databases()

        for name_base, data in bases.items():
            database_builder: DatabaseBuilder = DatabaseBuilder(name_base)

            database_builder\
                .set_host(data['host'])\
                .set_port(data['port'])\
                .set_credentials(data['username'], data['password'])\
                .set_dbname(data['dbname'])\
                .set_dialect(data['dialect'])\
                .set_drives(data.get('drive_default'), data.get('data_async'))\
            
            if data.get('debug'):
                database_builder.set_debug(True)

            if data.get('async'):
                database_builder.set_async(True)

            database: Database = database_builder.build()

            databases.add_base(database)

        return databases

    @staticmethod
    def __create_amqp() -> AMQP:
        return AMQP()

    @classmethod
    def create(
        cls,
        http_props: MappingDict,
        cli_props: MappingDict,
        databases_props: MappingDict,
        amqp_props: MappingDict = {}
    ) -> Server:
        http: HTTP = cls.__create_http(**http_props)

        cli: ControllerTaskManagers = cls.__create_cli(**cli_props)

        databases: Databases = cls.__create_databases(**databases_props)

        amqp: AMQP = cls.__create_amqp()

        return Server(
            http,
            cli,
            databases,
            amqp
        )



