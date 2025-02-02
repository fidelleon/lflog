"""Create lotw_users table

Revision ID: 9f1011424c55
Revises:
Create Date: 2025-02-02 17:10:37.413704

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '9f1011424c55'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade():
    op.create_table(
        'lotw_users',
        sa.Column('callsign', sa.String(50), primary_key=True),
        sa.Column('date_from', sa.DateTime(), nullable=False),
    )


def downgrade():
    op.drop_table('lotw_users')
