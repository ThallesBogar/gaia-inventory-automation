"""add_puma_irrigations_table

Revision ID: 58948a692c42
Revises: 0fe582a5bf66
Create Date: 2025-02-16 19:44:09.127784

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa
from migrations.helpers import get_updated_at_trigger_executable, get_drop_trigger_executable


# revision identifiers, used by Alembic.
revision: str = '58948a692c42'
down_revision: Union[str, None] = '0fe582a5bf66'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('puma_irrigations',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('field_id', sa.UUID(), nullable=True),
    sa.Column('irrigation_type', sa.String(length=50), nullable=True),
    sa.Column('irrigation_area', sa.DECIMAL(precision=8, scale=2), nullable=True),
    sa.Column('irrigation_date', sa.Date(), nullable=True),
    sa.Column('irrigation_rate', sa.DECIMAL(precision=8, scale=2), nullable=True),
    sa.Column('energy_consumption', sa.DECIMAL(precision=8, scale=2), nullable=True),
    sa.Column('energy_consumption_unit', sa.String(length=10), nullable=True),
    sa.Column('energy_type', sa.String(length=50), nullable=True),
    sa.Column('irrigation_field_percentage', sa.DECIMAL(precision=5, scale=2), nullable=True),
    sa.Column('created_at', sa.DateTime(timezone=True), server_default=sa.text('now()'), nullable=True),
    sa.Column('updated_at', sa.DateTime(timezone=True), server_default=sa.text('now()'), nullable=True),
    sa.ForeignKeyConstraint(['field_id'], ['fields.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###

    # Add trigger
    op.execute(get_updated_at_trigger_executable(trigger_name='puma_irrigations_set_updated_at_on_update', table_name='puma_irrigations'))


def downgrade() -> None:
    op.execute(get_drop_trigger_executable(trigger_name='puma_irrigations_set_updated_at_on_update', table_name='puma_irrigations'))
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('puma_irrigations')
    # ### end Alembic commands ###
