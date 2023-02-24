from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column
from datetime import datetime
from patterns.models import BaseModel


class User(BaseModel):
    __tablename__: str = "usuarios"

    name: Mapped[str] = mapped_column(String(100), nullable=False)
    email: Mapped[str] = mapped_column(String(300), nullable=False, unique=True)
    password: Mapped[str] = mapped_column(String(50), nullable=False)
    path: Mapped[str] = mapped_column(nullable=False)
    created: Mapped[datetime] = mapped_column(default=datetime.now)
