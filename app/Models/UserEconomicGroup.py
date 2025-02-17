from sqlalchemy import Column, Integer, ForeignKey, UUID, func, DateTime

from app.Models.Base import Base


class UserEconomicGroup(Base):
    __tablename__ = 'users_economic_groups'

    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('users.id'), nullable=False)
    economic_group_id = Column(UUID(as_uuid=True), ForeignKey('economic_groups.id'), nullable=False)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), server_default=func.now())
