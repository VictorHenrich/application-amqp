from dataclasses import dataclass
from typing import Union, Mapping, Any

from .http import HTTP
from .cli import ControllerTaskManagers
from .database import Databases, DatabaseBuilder, Database
from .amqp import AMQP



@dataclass
class Server:
    http: HTTP
    cli: ControllerTaskManagers
    database: Databases
    amqp: AMQP



class ServerFactory:
    @staticmethod
    def __create_http(
        host: str,
        port: Union[str, int],
        secret_key: str,
        debug: bool
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
        version: Union[float, str], 
        description: str,
        usage: str
    ) -> ControllerTaskManagers:
        return ControllerTaskManagers(
            name,
            version,
            description,
            usage
        )

    @staticmethod
    def __create_databases(
        bases: Mapping[str, Mapping[str, Any]]
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
    def __create_amqp(

    ) -> AMQP:
        return AMQP()

    @classmethod
    def create(
        cls,
        http_props: Mapping[str, Any],
        cli_props: Mapping[str, Any],
        databases_props: Mapping[str, Any],
        amqp_props: Mapping[str, Any]
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



