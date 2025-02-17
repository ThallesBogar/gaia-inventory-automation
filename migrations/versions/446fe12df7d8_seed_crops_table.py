"""seed_crops_table

Revision ID: 446fe12df7d8
Revises: 58948a692c42
Create Date: 2025-02-17 17:39:51.114616

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa
from sqlalchemy.orm import Session

from app.Models.Crop import Crop

# revision identifiers, used by Alembic.
revision: str = '446fe12df7d8'
down_revision: Union[str, None] = '58948a692c42'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None

def upgrade() -> None:
    bind = op.get_bind()
    session = Session(bind=bind)

    crops = [
        Crop(slug='soybeans', labels={'es': 'Soja'}),
        Crop(slug='corn', labels={'es': 'Maíz'}),
        Crop(slug='cotton', labels={'es': 'Algodón'}),
    ]

    session.add_all(crops)
    session.commit()


def downgrade() -> None:
    bind = op.get_bind()
    session = Session(bind=bind)

    session.query(Crop).filter(Crop.slug.in_(['soybeans', 'corn', 'cotton'])).delete(synchronize_session=False)
    session.commit()
