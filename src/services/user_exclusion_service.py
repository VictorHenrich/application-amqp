from dataclasses import dataclass

from start import app
from models import User
from patterns.repositories import IDeleteRepository
from repositories import UserDeleteRepository, UserDeleteRepositoryProps


@dataclass
class UserExclusionServiceProps:
    user: User


class UserExclusionService:
    def execute(self, args: UserExclusionServiceProps) -> None:
        with app.databases.create_session() as session:
            user_delete_repository: IDeleteRepository[
                UserDeleteRepositoryProps, None
            ] = UserDeleteRepository(session)

            user_delete_repository.delete(args)
