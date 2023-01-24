from sqlalchemy import (
    Column,
    String,
    DateTime,
    ForeignKey,
    Integer
)
from datetime import datetime
from patterns.models import BaseModel
from .user import User


class Drive(BaseModel):
    __tablename__: str = "arquivos"
    name: str = Column(String(200), nullable=False)
    id_user: int = Column(Integer, ForeignKey(f"{User.__tablename__}.id"))
    path: str = Column(String(1000), nullable=False)
    created: datetime = Column(DateTime, default=datetime.now)