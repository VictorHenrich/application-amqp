from typing import Mapping, Any
from server.amqp import AMQPConsumer
from start import app



@app.amqp.add_consumer("consumer", "queue_teste", ack=False)
class ConsumerTeste(AMQPConsumer):
    def on_message_queue(self, body: bytes, **kwargs: Mapping[str, Any]) -> None:
        print("MENSAGEM RECEBIDA COM SUCESSO!")
        print(body)
