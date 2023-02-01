from typing import Mapping, Any
from dataclasses import dataclass

from start import app
from server.amqp import AMQPConsumer
from patterns.service import IService
from services.access_creation_service import (
    AccessCreationService,
    AccessCreationServiceProps,
)


@dataclass
class ConsumerAccessCreationPayload:
    user_uuid: str
    drive_uuid: str
    operation: str


@app.amqp.add_consumer(
    "consumer_access_creation",
    "queue_access_creation",
    ack=True,
    data_class=ConsumerAccessCreationPayload,
)
class ConsumerAccessCreation(AMQPConsumer):
    def on_message_queue(
        self, body: ConsumerAccessCreationPayload, **kwargs: Mapping[str, Any]
    ) -> None:
        access_creation_props: AccessCreationServiceProps = AccessCreationServiceProps(
            body.user_uuid, body.drive_uuid, body.operation
        )

        access_creation_service: IService[
            AccessCreationServiceProps, None
        ] = AccessCreationService()

        access_creation_service.execute(access_creation_props)
