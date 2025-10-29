"""alter user table

Revision ID: aa00b9fe4599
Revises: 745a0def7c67
Create Date: 2025-10-29 14:44:42.685539

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'aa00b9fe4599'
down_revision: Union[str, Sequence[str], None] = '745a0def7c67'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    op.execute("""
                ALTER TABLE users
               ADD COLUMN gender varchar(100) DEFAULT 'male'
    """)
    pass

def downgrade() -> None:
    """Downgrade schema."""
    op.execute("""
                ALTER TABLE users
               DROP COLUMN gender
    """)
    pass
