import uuid

from sqlalchemy import Column, UUID, ForeignKey, String, DECIMAL, func, DateTime

from app.Models.Base import Base


class Field(Base):
    __tablename__ = 'fields'

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    program_id = Column(UUID(as_uuid=True), ForeignKey('programs.id'), nullable=False)
    farm_id = Column(UUID(as_uuid=True), ForeignKey('farms.id'), nullable=False)
    name = Column(String(50), nullable=False)
    area = Column(DECIMAL(8, 2), nullable=False)
    latitude = Column(String(50), nullable=False)
    longitude = Column(String(50), nullable=False)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), server_default=func.now())