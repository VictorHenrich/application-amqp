from typing import Mapping, Any
from pika import ConnectionParameters
from dataclasses import dataclass
from start import app
from server.amqp import AMQPConsumer, ConnectionBuilder
from services import DriveCreationService, DriveCreateServiceProps
from patterns.service import IService


@dataclass
class PayloadDriveCreation:
    filename: str
    path: str
    user_uuid: str


connection: ConnectionParameters = (
    ConnectionBuilder()
    .set_host("localhost")
    .set_port(5672)
    .set_credentials("guest", "guest")
    .build()
)


@app.amqp.add_consumer(
    "consumer_drive_creation",
    connection,
    "queue_drive_creation",
    data_class=PayloadDriveCreation,
)
class ConsumerDriveCreation(AMQPConsumer):
    def on_message_queue(self, body: PayloadDriveCreation, **kwargs: Mapping[str, Any]) -> None:        
        drive_creation_props: DriveCreateServiceProps = DriveCreateServiceProps(
            body.filename, body.path, body.user_uuid
        )

        drive_creation_service: IService[
            DriveCreateServiceProps, None
        ] = DriveCreationService()

        drive_creation_service.execute(drive_creation_props)
