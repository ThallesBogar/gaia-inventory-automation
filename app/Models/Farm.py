import uuid

from sqlalchemy import Column, UUID, String, ForeignKey, func, DateTime

from app.Models.Base import Base


class Farm(Base):
    __tablename__ = 'farms'

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    economic_group_id = Column(UUID(as_uuid=True), ForeignKey('economic_groups.id'), nullable=False)
    name = Column(String(50), nullable=False)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), server_default=func.now())