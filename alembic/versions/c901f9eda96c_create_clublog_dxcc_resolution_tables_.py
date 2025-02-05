"""Create clublog DXCC resolution tables - zone exceptions

Revision ID: c901f9eda96c
Revises: 78106e13b1fb
Create Date: 2025-02-05 17:27:25.361045

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'c901f9eda96c'
down_revision: Union[str, None] = '78106e13b1fb'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade():
    op.create_table(
        'clublog.zone_exceptions',
        sa.Column('record', sa.Integer(), nullable=False, index=True),
        sa.Column('call', sa.String(255), nullable=False, index=True),
        sa.Column('zone', sa.SmallInteger(), nullable=False, index=True),
        sa.Column('start', sa.DateTime(), nullable=True),
        sa.Column('end', sa.DateTime(), nullable=True),
    )


def downgrade():
    op.drop_table('clublog.zone_exceptions')
