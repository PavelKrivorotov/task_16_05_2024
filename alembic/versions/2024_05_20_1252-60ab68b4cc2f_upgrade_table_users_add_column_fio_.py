"""Upgrade table users. Add column fio_first_word

Revision ID: 60ab68b4cc2f
Revises: 4b352e695ac5
Create Date: 2024-05-20 12:52:00.957732

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '60ab68b4cc2f'
down_revision: Union[str, None] = '4b352e695ac5'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.execute("""
        ALTER TABLE users
            ADD COLUMN fio_first_word VARCHAR(1)
            GENERATED ALWAYS AS (left(fio, 1)) STORED;
    """)

    op.execute("""
        CREATE INDEX index_users_fio_first_word_btree
        ON users
        USING btree (fio_first_word);
    """)


def downgrade() -> None:
    op.drop_index('index_users_fio_first_word_btree', 'users')
    op.drop_column('users', 'fio_first_word')

