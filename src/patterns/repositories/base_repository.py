from abc import ABC
from typing import Union, TypeAlias
from sqlalchemy.orm import Session
from sqlalchemy.ext.asyncio import AsyncSession


SessionParam: TypeAlias = Union[Session, AsyncSession]


class BaseRepository(ABC):
    def __init__(self, session: SessionParam) -> None:
        self.__session: SessionParam = session

    @property
    def session(self) -> SessionParam:
        return self.__session
