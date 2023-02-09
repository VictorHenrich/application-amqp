from dataclasses import dataclass
from uuid import uuid4
from pathlib import Path

from start import app
from repositories import UserCreateRepository, UserCreateRepositoryProps
from patterns.repositories import ICreateRepository
from utils.constants import __PATH_DRIVES__


@dataclass
class UserCreationServiceProps:
    name: str
    email: str
    password: str


@dataclass
class UserCreate:
    name: str
    email: str
    password: str
    path: str


class UserCreationService:
    def execute(self, args: UserCreationServiceProps) -> None:
        with app.databases.create_session() as session:
            path: Path = Path(__PATH_DRIVES__) / str(uuid4())

            if not path.exists():
                path.mkdir()

            user_create_props: UserCreateRepositoryProps = UserCreate(
                name=args.name, email=args.email, password=args.password, path=path
            )

            user_create_repository: ICreateRepository[
                UserCreateRepositoryProps, None
            ] = UserCreateRepository(session)

            user_create_repository.create(user_create_props)
