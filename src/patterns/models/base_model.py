from sqlalchemy import (
    Column,
    Integer
)
from sqlalchemy.dialects.postgresql import UUID
from uuid import uuid4

from server.database import Database
from start import app



database: Database = app.databases.get_database()


class BaseModel(database.Model):
    __abstract__: bool = True
    id: int = Column(Integer, primary_key=True, auto_increment=True, nullable=False, unique=True)
    id_uuid: str = Column(UUID(False), unique=True, nullable=False, default=uuid4)