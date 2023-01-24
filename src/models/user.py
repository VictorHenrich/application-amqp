from sqlalchemy import (
    Column,
    String,
    DateTime
)
from datetime import datetime
from patterns.models import BaseModel


class User(BaseModel):
    __tablename__: str = "usuarios"
    name: str = Column(String(200), nullable=False)
    email: str = Column(String(200), nullable=False, unique=True)
    password: str = Column(String(50), nullable=False)
    created: datetime = Column(DateTime, default=datetime.now)