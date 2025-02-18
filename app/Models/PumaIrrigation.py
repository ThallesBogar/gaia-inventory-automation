from sqlalchemy import Column, Integer, UUID, ForeignKey, String, DECIMAL, Date, func, DateTime

from app.Models.Base import Base


class PumaIrrigation(Base):
    __tablename__ = 'puma_irrigations'

    id = Column(Integer, primary_key=True)
    field_id = Column(UUID(as_uuid=True), ForeignKey('fields.id'))
    crop_id = Column(Integer, ForeignKey('crops.id', name='puma_irrigations_crop_id_fkey'))
    season_id = Column(Integer, ForeignKey('seasons.id', name='puma_irrigations_season_id_fkey'))
    crop = Column(String(50))
    season_name = Column(String(50))
    season_year = Column(String(4))
    irrigation_type = Column(String(50))
    irrigation_area = Column(DECIMAL(8, 2))
    irrigation_date = Column(Date)
    irrigation_rate = Column(DECIMAL(8, 2))
    energy_consumption = Column(DECIMAL(8, 2))
    energy_consumption_unit = Column(String(10))
    energy_type = Column(String(50))
    irrigation_field_percentage = Column(DECIMAL(5, 2))
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), server_default=func.now())