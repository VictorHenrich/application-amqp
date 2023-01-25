from typing import Mapping, Any
from pika import ConnectionParameters
from server.amqp import AMQPConsumer, ConnectionBuilder
from start import app


connection: ConnectionParameters = (
    ConnectionBuilder()
    .set_host("localhost")
    .set_port(5672)
    .set_credentials("guest", "guest")
    .build()
)


@app.amqp.add_consumer("consumer", connection, "queue_teste", False)
class ConsumerTeste(AMQPConsumer):
    def on_message_queue(self, body: bytes, **kwargs: Mapping[str, Any]) -> None:
        print("MENSAGEM RECEBIDA COM SUCESSO!")
        print(body)
