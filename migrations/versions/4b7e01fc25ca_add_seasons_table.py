"""add_seasons_table

Revision ID: 4b7e01fc25ca
Revises: a4e14a5af05f
Create Date: 2025-02-16 19:32:18.406579

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql
from migrations.helpers import get_updated_at_trigger_executable, get_drop_trigger_executable

# revision identifiers, used by Alembic.
revision: str = '4b7e01fc25ca'
down_revision: Union[str, None] = 'a4e14a5af05f'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('seasons',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('slug', sa.String(length=50), nullable=False),
    sa.Column('year', sa.String(length=4), nullable=False),
    sa.Column('labels', postgresql.JSONB(astext_type=sa.Text()), nullable=False),
    sa.Column('created_at', sa.DateTime(timezone=True), server_default=sa.text('now()'), nullable=True),
    sa.Column('updated_at', sa.DateTime(timezone=True), server_default=sa.text('now()'), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('slug', 'year', name='uix_seasons_slug_year')
    )
    # ### end Alembic commands ###

    op.execute(get_updated_at_trigger_executable(trigger_name='seasons_set_updated_at_on_update', table_name='seasons'))



def downgrade() -> None:
    op.execute(get_drop_trigger_executable(trigger_name='seasons_set_updated_at_on_update', table_name='seasons'))
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('seasons')
    # ### end Alembic commands ###
