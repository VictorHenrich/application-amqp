from dataclasses import dataclass

from .http import HTTP
from .cli import ControllerTaskManagers
from .database import Databases
from .amqp import AMQP



@dataclass
class Server:
    http: HTTP
    cli: ControllerTaskManagers
    database: Databases
    amqp: AMQP

