"""seed_seasons_table

Revision ID: c447aaf06cce
Revises: 446fe12df7d8
Create Date: 2025-02-17 18:12:22.513363

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa
from sqlalchemy.orm import Session

from app.Models.Season import Season

# revision identifiers, used by Alembic.
revision: str = 'c447aaf06cce'
down_revision: Union[str, None] = '446fe12df7d8'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None

created_ids = []

def upgrade() -> None:
    bind = op.get_bind()
    session = Session(bind=bind)

    seasons = [
        Season(slug='sum', year='2024', labels={'es': '24-25'})
    ]

    session.add_all(seasons)
    session.commit()


def downgrade() -> None:
    bind = op.get_bind()
    session = Session(bind=bind)

    session.query(Season).filter(
        Season.slug == 'sum',
        Season.year == '2024',
    ).delete()

    session.commit()
