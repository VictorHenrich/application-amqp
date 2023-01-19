from typing import Mapping, Any, Optional
from abc import ABC, abstractmethod
from pika import ConnectionParameters
from pika.adapters.blocking_connection import BlockingChannel
from .abstract_amqp import AbstractAMQP



class AMQPConsumer(AbstractAMQP, ABC):

    def __init__(
        self,
        consumer_name: str,
        connection: ConnectionParameters,
        queue_name: str,
        ack: bool = True,
        arguments: Optional[Mapping[str, Any]] = None
    ) -> None:
        super().__init__(connection)

        self.__consumer_name: str = consumer_name
        self.__queue_name: str = queue_name
        self.__ack: bool = ack
        self.__arguments: Optional[Mapping[str, Any]] = arguments

    def start(self) -> None:
        channel: BlockingChannel = self.get_channel()

        channel.queue_declare(
            queue=self.__queue_name,
            durable=True,
            arguments=self.__arguments
        )

        channel.basic_consume(
            queue=self.__queue_name,
            auto_ack=self.__ack,
            on_message_callback=self.on_message_queue,
            arguments=self.__arguments
        )

        print(f'Consumer ${self.__consumer_name} running in ${self.connection_parameters.host}:${self.connection_parameters.port}')

        channel.start_consuming()

    @abstractmethod
    def on_message_queue(self, ch, method, properties, body: bytes) -> None:
        pass