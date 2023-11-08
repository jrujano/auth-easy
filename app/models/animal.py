import enum
from sqlalchemy import (
    Column,
    Integer,
    String,
    ForeignKey,
    Boolean,
    Date,
    DateTime,
    Enum,
)
from sqlalchemy.sql import func
from app.db.base import Base


class SexEnum(enum.Enum):
    Macho = "Macho"
    Hembra = "Hembra"


class Animal(Base):
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True, nullable=False)
    code = Column(String, nullable=True)
    sex = Column(Enum(SexEnum), nullable=True)
    birth_date = Column(Date, nullable=True)
    time_created = Column(DateTime(timezone=True), server_default=func.now())
    time_updated = Column(DateTime(timezone=True), onupdate=func.now())
