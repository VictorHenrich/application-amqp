from sqlalchemy import String, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column
from datetime import datetime
from patterns.models import BaseModel
from .user import User
from .drive import Drive


class Access(BaseModel):
    __tablename__: str = "acessos"

    operation: Mapped[str] = mapped_column(String(20), nullable=False)
    id_user: Mapped[int] = mapped_column(ForeignKey(f"{User.__tablename__}.id"))
    id_drive: Mapped[int] = mapped_column(ForeignKey(f"{Drive.__tablename__}.id"))
    created: Mapped[datetime] = mapped_column(default=datetime.now)
