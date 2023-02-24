from sqlalchemy import Integer
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy.dialects.postgresql import UUID
from uuid import uuid4

from server.database import Base
from start import app


class BaseModel(Base):
    __abstract__: bool = True
    id: Mapped[int] = mapped_column(
        primary_key=True, autoincrement=True, unique=True, nullable=False
    )
    id_uuid: Mapped[str] = mapped_column(
        UUID(False), unique=True, nullable=False, default=lambda _: str(uuid4())
    )
