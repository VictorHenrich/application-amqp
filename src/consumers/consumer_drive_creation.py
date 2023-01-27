from typing import Mapping, Any
from dataclasses import dataclass
from start import app
from server.amqp import AMQPConsumer
from services import DriveCreationService, DriveCreateServiceProps
from patterns.service import IService


@dataclass
class ConsumerDriveCreationPayload:
    filename: str
    path: str
    user_uuid: str


@app.amqp.add_consumer(
    "consumer_drive_creation",
    "queue_drive_creation",
    ack=True,
    data_class=ConsumerDriveCreationPayload,
)
class ConsumerDriveCreation(AMQPConsumer):
    def on_message_queue(
        self, body: ConsumerDriveCreationPayload, **kwargs: Mapping[str, Any]
    ) -> None:
        drive_creation_props: DriveCreateServiceProps = DriveCreateServiceProps(
            body.filename, body.path, body.user_uuid
        )

        drive_creation_service: IService[
            DriveCreateServiceProps, None
        ] = DriveCreationService()

        drive_creation_service.execute(drive_creation_props)
