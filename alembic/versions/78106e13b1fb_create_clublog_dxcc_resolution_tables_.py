"""Create clublog DXCC resolution tables - invalid operations

Revision ID: 78106e13b1fb
Revises: f5c057c21335
Create Date: 2025-02-05 17:03:49.649795

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '78106e13b1fb'
down_revision: Union[str, None] = 'f5c057c21335'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade():
    op.create_table(
        'clublog.invalid',
        sa.Column('record', sa.Integer(), nullable=False, index=True),
        sa.Column('call', sa.String(255), nullable=False),
        sa.Column('start', sa.DateTime(), nullable=True),
        sa.Column('end', sa.DateTime(), nullable=True),
    )


def downgrade():
    op.drop_table('clublog.invalid')
