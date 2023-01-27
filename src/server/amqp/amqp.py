from typing import Mapping, Optional, Any, Callable, TypeAlias, List, Type
from threading import Thread
from pika import ConnectionParameters

from .consumer import AMQPConsumer


TypeAMQPConsumer: TypeAlias = type[AMQPConsumer]
ReturnDecoratorAddConsumer: TypeAlias = Callable[[TypeAMQPConsumer], TypeAMQPConsumer]
ConnectionParametersOptional: TypeAlias = Optional[ConnectionParameters]


class AMQP:
    def __init__(self, default_connection: ConnectionParametersOptional) -> None:
        self.__consumers: Mapping[str, AMQPConsumer] = {}
        self.__default_connection: ConnectionParametersOptional = default_connection

    @property
    def default_connection(self) -> ConnectionParametersOptional:
        return self.__default_connection

    def add_consumer(
        self,
        consumer_name: str,
        queue_name: str,
        ack: bool = True,
        connection: ConnectionParametersOptional = None,
        arguments: Optional[Mapping[str, Any]] = None,
        data_class: Optional[Type] = None,
    ) -> ReturnDecoratorAddConsumer:
        def wrapper(cls: TypeAMQPConsumer) -> TypeAMQPConsumer:

            connection_: ConnectionParameters = connection or self.__default_connection

            consumer: AMQPConsumer = cls(
                consumer_name, connection_, queue_name, ack, arguments, data_class
            )

            self.__consumers[consumer.name] = consumer

            cls

        return wrapper

    def start_consumers(self) -> None:
        threads: List[Thread] = [
            Thread(target=consumer.start) for consumer in self.__consumers.values()
        ]

        [thread.start() for thread in threads]
