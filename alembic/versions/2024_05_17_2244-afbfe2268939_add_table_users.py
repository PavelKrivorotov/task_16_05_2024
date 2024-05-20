"""Add table users

Revision ID: afbfe2268939
Revises: 
Create Date: 2024-05-17 22:44:50.519816

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'afbfe2268939'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ###
    op.create_table(
        'users',
        sa.Column('id', sa.Integer(), primary_key=True),
        sa.Column('fio', sa.String(300), nullable=False),
        sa.Column('dob', sa.Date(), nullable=False),
        sa.Column('sex', sa.String(6), nullable=False)
    )

    op.drop_constraint('users_pkey', 'users')
    # ###


def downgrade() -> None:
    # ###
    op.drop_table('users')
    # ###
