"""alter user table

Revision ID: 745a0def7c67
Revises: 
Create Date: 2025-10-29 11:21:04.881653

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '745a0def7c67'
down_revision: Union[str, Sequence[str], None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    op.execute("""
                ALTER TABLE users
               ADD COLUMN userType varchar(100) DEFAULT 'student'
""")
    pass


def downgrade() -> None:
    """Downgrade schema."""
    op.execute("""
                ALTER TABLE users
               DROP COLUMN userType
""")
    pass

