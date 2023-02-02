from utils import EnvUtil


env_values = EnvUtil.get_values()


__HTTP__ = {
    "host": env_values["HTTP_HOST"],
    "port": env_values["HTTP_PORT"],
    "debug": bool(eval(env_values["HTTP_DEBUG"])),
    "secret_key": env_values["HTTP_SECRET_KEY"],
}


__CLI__ = {
    "managers": ["api", "databases", "consumers"],
    "name": env_values["CLI_NAME"],
    "version": float(env_values["CLI_VERSION"]),
    "description": env_values["CLI_DESCRIPTION"],
}


__DATABASES__ = {
    "bases": {
        "main": {
            "host": env_values["DATABASE_MAIN_HOST"],
            "port": env_values["DATABASE_MAIN_PORT"],
            "username": env_values["DATABASE_MAIN_USERNAME"],
            "password": env_values["DATABASE_MAIN_PASSWORD"],
            "dbname": env_values["DATABASE_MAIN_DBNAME"],
            "dialect": env_values["DATABASE_MAIN_DIALECT"],
            "drive_default": env_values["DATABASE_MAIN_DRIVE_DEFAULT"],
            "drive_async": env_values["DATABASE_MAIN_DRIVE_ASYNC"],
        }
    }
}


__AMQP__ = {
    "default_connection": {
        "host": env_values["AMQP_HOST"],
        "port": env_values["AMQP_PORT"],
        "username": env_values["AMQP_USERNAME"],
        "password": env_values["AMQP_PASSWORD"],
    }
}


__SMTP__ = {
    "host": env_values["SMTP_HOST"],
    "port": env_values["SMTP_PORT"],
    "username": env_values["SMTP_USERNAME"],
    "password": env_values["SMTP_PASSWORD"],
    "tls": bool(eval(env_values["SMTP_TLS"])),
    "ssl": bool(eval(env_values["SMTP_SSL"])),
}
