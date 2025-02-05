"""Create clublog DXCC resolution tables - exceptions

Revision ID: 70a1ac906abf
Revises: 373fdbcfc23b
Create Date: 2025-02-05 16:18:36.218952

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '70a1ac906abf'
down_revision: Union[str, None] = '373fdbcfc23b'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade():
    op.create_table(
        'clublog.exceptions',
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
    op.drop_table('clublog.exceptions')
