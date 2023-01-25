from typing import Mapping, Optional, Any, Callable, TypeAlias, List
from threading import Thread
from pika import ConnectionParameters

from .consumer import AMQPConsumer


TypeAMQPConsumer: TypeAlias = type[AMQPConsumer]
ReturnDecoratorAddConsumer: TypeAlias = Callable[[TypeAMQPConsumer], TypeAMQPConsumer]


class AMQP:
    def __init__(self) -> None:
        self.__consumers: Mapping[str, AMQPConsumer] = {}

    def add_consumer(
        self,
        consumer_name: str,
        connection: ConnectionParameters,
        queue_name: str,
        ack: bool = True,
        arguments: Optional[Mapping[str, Any]] = None,
    ) -> ReturnDecoratorAddConsumer:
        def wrapper(cls: TypeAMQPConsumer) -> TypeAMQPConsumer:
            consumer: AMQPConsumer = cls(
                consumer_name, connection, queue_name, ack, arguments
            )

            self.__consumers[consumer.name] = consumer

            cls

        return wrapper

    def start_consumers(self) -> None:
        threads: List[Thread] = [
            Thread(target=consumer.start) for consumer in self.__consumers.values()
        ]

        [thread.start() for thread in threads]
