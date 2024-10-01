"""Initial migration

Revision ID: d70ea89a469b
Revises: 
Create Date: 2024-10-01 15:19:39.769897

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'd70ea89a469b'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # Create the 'users' table
    op.create_table(
        'users',
        sa.Column('id', sa.Integer, primary_key=True),
        sa.Column('name', sa.String(), nullable=False, server_default="dude"),
        sa.Column('wallet', sa.Float(), nullable=False, server_default="0"),
        sa.Column('email', sa.String(), nullable=False, unique=True, index=True),
        sa.Column('hashed_password', sa.String(), nullable=False),
        sa.Column('is_active', sa.Boolean(), nullable=False, server_default=sa.text('true')),
    )


def downgrade() -> None:
    # Drop the 'users' table if we downgrade
    op.drop_table('users')
