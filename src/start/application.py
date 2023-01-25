from server import ServerFactory, Server
from .config import __DATABASES__, __HTTP__, __CLI__

app: Server = ServerFactory.create(
    cli_props=__CLI__, databases_props=__DATABASES__, http_props=__HTTP__
)
