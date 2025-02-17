import uuid

from sqlalchemy import Column, String, DateTime, func, UUID

from app.Models.Base import Base


class Program(Base):
    __tablename__ = 'programs'

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    name = Column(String(50), nullable=False)
    slug = Column(String(50), unique=True, nullable=False)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), server_default=func.now())