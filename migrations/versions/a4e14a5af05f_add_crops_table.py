"""add_crops_table

Revision ID: a4e14a5af05f
Revises: 94d12bcef9b5
Create Date: 2025-02-16 19:20:28.958536

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql
from migrations.helpers import get_updated_at_trigger_executable, get_drop_trigger_executable

# revision identifiers, used by Alembic.
revision: str = 'a4e14a5af05f'
down_revision: Union[str, None] = '94d12bcef9b5'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('crops',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('slug', sa.String(length=50), nullable=False),
    sa.Column('labels', postgresql.JSONB(astext_type=sa.Text()), nullable=False),
    sa.Column('created_at', sa.DateTime(timezone=True), server_default=sa.text('now()'), nullable=True),
    sa.Column('updated_at', sa.DateTime(timezone=True), server_default=sa.text('now()'), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('slug')
    )
    # ### end Alembic commands ###

    op.execute(get_updated_at_trigger_executable(trigger_name='crops_set_updated_at_on_update', table_name='crops'))


def downgrade() -> None:
    op.execute(get_drop_trigger_executable(trigger_name='crops_set_updated_at_on_update', table_name='crops'))
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('crops')
    # ### end Alembic commands ###
