"""Create clublog DXCC resolution tables

Revision ID: 373fdbcfc23b
Revises: 49187d57ffe6
Create Date: 2025-02-03 19:10:26.831617

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '373fdbcfc23b'
down_revision: Union[str, None] = '49187d57ffe6'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade():
    op.create_table(
        'clublog.entities',
        sa.Column('adif', sa.SmallInteger(), nullable=False, index=True),
        sa.Column('name', sa.String(255), nullable=False),
        sa.Column('prefix', sa.String(255), nullable=False, index=True),
        sa.Column('deleted', sa.Boolean(), index=True, nullable=False, default=True),
        sa.Column('cqz', sa.SmallInteger(), nullable=True),
        sa.Column('cont', sa.String(255), nullable=True),
        sa.Column('long', sa.Float(), nullable=True),
        sa.Column('lat', sa.Float(), nullable=True),
        sa.Column('start', sa.DateTime(), nullable=True),
        sa.Column('end', sa.DateTime(), nullable=True),
        sa.Column('whitelisted', sa.Boolean(), nullable=False, default=True),
        sa.Column('whitelist_start', sa.DateTime(), nullable=True),
        sa.Column('whitelist_end', sa.DateTime(), nullable=True),
    )


def downgrade():
    op.drop_table('clublog.entities')
