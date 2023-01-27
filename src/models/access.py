from sqlalchemy import Column, String, DateTime, ForeignKey, Integer
from datetime import datetime
from patterns.models import BaseModel
from .user import User
from .drive import Drive


class Access(BaseModel):
    __tablename__: str = "acessos"
    operation: str = Column(String(20), nullable=False)
    id_user: int = Column(Integer, ForeignKey(f"{User.__tablename__}.id"))
    id_drive: int = Column(Integer, ForeignKey(f"{Drive.__tablename__}.id"))
    created: datetime = Column(DateTime, default=datetime.now)
