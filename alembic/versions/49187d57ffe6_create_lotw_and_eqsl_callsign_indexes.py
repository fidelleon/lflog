"""Create lotw and eqsl callsign indexes

Revision ID: 49187d57ffe6
Revises: c03708a52c83
Create Date: 2025-02-02 19:03:40.160007

"""
from typing import Sequence, Union

from alembic import op


# revision identifiers, used by Alembic.
revision: str = '49187d57ffe6'
down_revision: Union[str, None] = 'c03708a52c83'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_index('lotw_callsign_index', 'lotw_users', ['callsign'], unique=True)
    op.create_index('eqsl_callsign_index', 'eqsl_users', ['callsign'], unique=True)


def downgrade() -> None:
    op.drop_index('lotw_callsign_index', table_name='lotw_users')
    op.drop_index('eqsl_callsign_index', table_name='eqsl_users')
