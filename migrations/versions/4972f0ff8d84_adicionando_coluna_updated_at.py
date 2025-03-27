"""adicionando coluna updated_at

Revision ID: 4972f0ff8d84
Revises: fdb85cfd4a7a
Create Date: 2025-03-26 19:23:52.793677

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '4972f0ff8d84'
down_revision: Union[str, None] = 'fdb85cfd4a7a'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    op.add_column(
        'users', sa.Column('updated_at', sa.DateTime(), nullable=True)
    )

def downgrade() -> None:
    """Downgrade schema."""
    op.drop_column('users', 'updated_at')
