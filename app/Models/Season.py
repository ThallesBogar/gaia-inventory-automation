from sqlalchemy import UniqueConstraint, Column, String, Integer, func, DateTime
from sqlalchemy.dialects.postgresql import JSONB

from app.Models.Base import Base


class Season(Base):
    __tablename__ = 'seasons'
    __table_args__ = (
        UniqueConstraint('slug', 'year', name='uix_seasons_slug_year'),
    )

    id = Column(Integer, primary_key=True)
    slug = Column(String(50), nullable=False)
    year = Column(String(4), nullable=False)
    labels = Column(JSONB, nullable=False)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), server_default=func.now())