from sqlalchemy import String, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column
from datetime import datetime
from patterns.models import BaseModel
from .user import User


class Drive(BaseModel):
    __tablename__: str = "arquivos"

    name: Mapped[str] = mapped_column(String(200), nullable=False)
    id_user: Mapped[int] = mapped_column(ForeignKey(f"{User.__tablename__}.id"))
    path: Mapped[str] = mapped_column(nullable=False)
    created: Mapped[datetime] = mapped_column(default=datetime.now)
