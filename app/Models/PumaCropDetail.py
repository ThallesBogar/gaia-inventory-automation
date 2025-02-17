from sqlalchemy import Column, Integer, UUID, ForeignKey, String, DECIMAL, func, DateTime

from app.Models.Base import Base


class PumaCropDetail(Base):
    __tablename__ = 'puma_crop_details'

    id = Column(Integer, primary_key=True)
    field_id = Column(UUID(as_uuid=True), ForeignKey('fields.id'), nullable=False)
    crop_id = Column(Integer, ForeignKey('crops.id'), nullable=False)
    season_id = Column(Integer, ForeignKey('seasons.id'), nullable=False)
    crop_type = Column(String(50))
    planting_system = Column(String(50))
    harvest_yield = Column(Integer)
    harvest_residue_extraction = Column(Integer)
    harvest_burned_residues = Column(DECIMAL(5, 2))
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), server_default=func.now())