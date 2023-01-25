from dataclasses import dataclass
from patterns.repositories import BaseRepository
from models import User


@dataclass
class UserAuthRepositoryProps:
    email: str
    password: str


class UserAuthRepository(BaseRepository):
    def auth(self, args: UserAuthRepositoryProps) -> User:
        user: User = (
            self
            .session
            .query(User)
            .filter(
                User.email._upper() == args.email.upper(),
                User.password == args.password,
            )
            .first()
        )

        if not user:
            raise Exception("User not found!")

        return user
