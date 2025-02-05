"""Create clublog DXCC resolution tables - prefixes

Revision ID: f5c057c21335
Revises: 70a1ac906abf
Create Date: 2025-02-05 16:36:39.024194

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'f5c057c21335'
down_revision: Union[str, None] = '70a1ac906abf'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade():
    op.create_table(
        'clublog.prefixes',
        sa.Column('record', sa.Integer(), nullable=False, index=True),
        sa.Column('call', sa.String(255), nullable=False),
        sa.Column('entity', sa.String(255), nullable=False, index=True),
        sa.Column('adif', sa.SmallInteger(), nullable=False, index=True),
        sa.Column('cqz', sa.SmallInteger(), nullable=True),
        sa.Column('cont', sa.String(255), nullable=True),
        sa.Column('long', sa.Float(), nullable=True),
        sa.Column('lat', sa.Float(), nullable=True),
        sa.Column('start', sa.DateTime(), nullable=True),
        sa.Column('end', sa.DateTime(), nullable=True),
    )


def downgrade():
    op.drop_table('clublog.prefixes')
