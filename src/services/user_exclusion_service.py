from dataclasses import dataclass

from start import app
from models import User
from patterns.repositories import IDeleteRepository, IFindRepository
from repositories import (
    UserDeleteRepository,
    UserDeleteRepositoryProps,
    UserFindRepository,
    UserFindRepositoryProps,
)


@dataclass
class UserExclusionServiceProps:
    user_uuid: str


@dataclass
class UserDeleteProps:
    user: User


class UserExclusionService:
    def execute(self, args: UserExclusionServiceProps) -> None:
        with app.databases.create_session() as session:
            user_find_repository: IFindRepository[
                UserFindRepositoryProps, User
            ] = UserFindRepository(session)

            user: User = user_find_repository.find(args)

            user_delete_props: UserDeleteRepositoryProps = UserDeleteProps(user)

            user_delete_repository: IDeleteRepository[
                UserDeleteRepositoryProps, None
            ] = UserDeleteRepository(session)

            user_delete_repository.delete(user_delete_props)

            session.commit()
