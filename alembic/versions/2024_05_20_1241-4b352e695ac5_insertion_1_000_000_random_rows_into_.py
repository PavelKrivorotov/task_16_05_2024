"""Insertion 1`000`000 random rows into the users

Revision ID: 4b352e695ac5
Revises: 7e4483c4d895
Create Date: 2024-05-20 12:41:03.716702

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '4b352e695ac5'
down_revision: Union[str, None] = '7e4483c4d895'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ###
    op.execute("""
        INSERT INTO users (fio, dob, sex)
        (
            SELECT random_fio() AS fio, random_dob() AS dob, random_sex() AS sex
            FROM generate_series(1, 1000000)
        );
    """)
    # ###


def downgrade() -> None:
    # ###
    op.execute('DELETE FROM users;')
    # ###

