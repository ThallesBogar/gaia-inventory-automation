from sqlalchemy import Column, Integer, UUID, ForeignKey, String, Date, DECIMAL, func, DateTime

from app.Models.Base import Base


class PumaLabor(Base):
    __tablename__ = 'puma_labors'

    id = Column(Integer, primary_key=True)
    field_id = Column(UUID(as_uuid=True), ForeignKey('fields.id'), nullable=False)
    labor_type = Column(String(50))
    labor_date = Column(Date, nullable=False)
    labor_quantity_day = Column(Integer)
    labor_area = Column(DECIMAL(8, 2), nullable=False)
    seed_rate = Column(DECIMAL(8, 2))
    grain_moisture = Column(DECIMAL(5, 2))
    crop_id = Column(Integer, ForeignKey('crops.id'))
    season_id = Column(Integer, ForeignKey('seasons.id'))
    product_type = Column(String(50))
    product_name = Column(String(255))
    product_commercial_name = Column(String(255))
    product_dose = Column(DECIMAL(5, 2))
    product_dose_unit = Column(String(50))
    data_source = Column(String(50), nullable=False)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), server_default=func.now())