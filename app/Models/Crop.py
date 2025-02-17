from sqlalchemy import Column, Integer, String, func, DateTime
from sqlalchemy.dialects.postgresql import JSONB

from app.Models.Base import Base


class Crop(Base):
    __tablename__ = 'crops'

    id = Column(Integer, primary_key=True)
    slug = Column(String(50), unique=True, nullable=False)
    labels = Column(JSONB, nullable=False)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), server_default=func.now())