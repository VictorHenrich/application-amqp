from dataclasses import dataclass

from start import app
from models import User
from consumers import UserExclusionConsumerPayload
from utils import FileUtil


@dataclass
class UserFolderExclusionServiceProps:
    user: User


class UserFolderExclusionService:
    def execute(self, args: UserFolderExclusionServiceProps) -> None:
        FileUtil.remove(args.user.path)

        publisher_payload: UserExclusionConsumerPayload = UserExclusionConsumerPayload(
            args.user.id_uuid
        )

        app.amqp.create_publisher(
            "publisher_user_folder_exclusion",
            "exchange_user_folder_exclusion",
            publisher_payload.__dict__,
        )
