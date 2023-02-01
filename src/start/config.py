__HTTP__ = {"host": "localhost", "port": 3000, "debug": True, "secret_key": "Teste"}


__CLI__ = {
    "managers": ["api", "consumers", "databases"],
    "name": "CLI DRIVE API AMQP",
    "version": 1.3,
    "description": "Terminal de comandos para a aplicação Drive API",
}


__DATABASES__ = {
    "bases": {
        "main": {
            "host": "localhost",
            "port": 5432,
            "username": "postgres",
            "password": "1234",
            "dbname": "banco_teste",
            "dialect": "postgresql",
            "drive_default": "psycopg2",
            "drive_async": "asyncpg",
        }
    }
}


__AMQP__ = {
    "default_connection": {
        "host": "localhost",
        "port": 5672,
        "username": "guest",
        "password": "guest",
    }
}


__SMTP__ = {
    "host": "smtp.gmail.com",
    "port": 587,
    "username": "",
    "password": "",
    "tls": True,
    "ssl": False,
}
