from typing import Mapping, Any
from dataclasses import dataclass

from start import app
from server.amqp import AMQPConsumer
from patterns.service import IService
from services.user_exclusion_service import (
    UserExclusionService,
    UserExclusionServiceProps,
)


@dataclass
class UserExclusionConsumerPayload:
    user_uuid: str


@app.amqp.add_consumer(
    "user_folder_exclusion_consumer",
    "queue_user_folder_exclusion",
    ack=True,
    data_class=UserExclusionConsumerPayload,
)
class UserExclusionConsumer(AMQPConsumer):
    def on_message_queue(
        self, body: UserExclusionConsumerPayload, **kwargs: Mapping[str, Any]
    ) -> None:
        user_exclusion_props: UserExclusionServiceProps = UserExclusionServiceProps(
            body.user_uuid
        )

        user_exclusion_service: IService[
            UserExclusionServiceProps, None
        ] = UserExclusionService()

        user_exclusion_service.execute(user_exclusion_props)
