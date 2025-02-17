import uuid

from sqlalchemy import Column, UUID, String, DateTime, func

from app.Models.Base import Base


class EconomicGroup(Base):
    __tablename__ = 'economic_groups'

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    leaf_user_id = Column(UUID(as_uuid=True))
    name = Column(String(50), nullable=False)
    slug = Column(String(50), unique=True, nullable=False)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), server_default=func.now())