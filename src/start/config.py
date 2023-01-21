
__HTTP__ = {
    "host": "localhost",
    "port": 3000,
    "debug": True,
    "secret_key": "Teste"
}

__CLI__ = {
    "managers": ['api'],
    "name": "CLI DRIVE API AMQP",
    "version": 1.0,
    "description": "Terminal de comandos para a aplicação Drive API"
}

__DATABASES__ = {
    "bases": {
        "main":{
            "host": "localhost",
            "port": 5432,
            "username": "postgres",
            "password": "1234",
            "dbname": "teste",
            "dialect": "postgresql",
            "drive_default": "psycopg2",
            "drive_async": "asyncpg"
        }
    }
}