"""Create eqsl_users table

Revision ID: c03708a52c83
Revises: 9f1011424c55
Create Date: 2025-02-02 18:30:57.622457

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'c03708a52c83'
down_revision: Union[str, None] = '9f1011424c55'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade():
    op.create_table(
        'eqsl_users',
        sa.Column('callsign', sa.String(50), primary_key=True),
        sa.Column('date_from', sa.DateTime(), nullable=False),
    )


def downgrade():
    op.drop_table('eqsl_users')
