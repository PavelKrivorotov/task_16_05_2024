"""Add functions: random_fio, random_dob, random_male

Revision ID: 7e4483c4d895
Revises: afbfe2268939
Create Date: 2024-05-20 11:46:07.120527

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '7e4483c4d895'
down_revision: Union[str, None] = 'afbfe2268939'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ###
    op.execute("""
        CREATE OR REPLACE FUNCTION random_fio() RETURNS TEXT AS
        $$
            DECLARE
                index_f INT;
                f TEXT[] := '{
                    "whittlee", "beasleye", "goodwine",
                    "houstons", "parryw", "langley",
                    "airaldii", "reviee", "caldwelle",
                    "strudwicke", "fishere"
                }';
               
                index_i INT;
                i TEXT[] := '{
                    "Lili", "Louella", "Wilfred",
                    "Jancis", "Stuart", "Melinda",
                    "Avery", "Wybert", "Nell",
                    "Edvin", "Leland"
                }';
               
                index_o INT;
                o TEXT[] := '{
                    "Monday", "Tuesday", "Wednesday",
                    "Thursday", "Friday", "Saturday",
                    "Sunday"
                }';
               
                fio TEXT;
            BEGIN
                index_f := round(random()*(array_length(f, 1) - 1));
                index_i := round(random()*(array_length(i, 1) - 1));
                index_o := round(random()*(array_length(o, 1) - 1));

                fio := chr(round(random()*25)::INT + 65)
                    || f[index_f + 1]
                    || ' '
                    || i[index_i + 1]
                    || ' '
                    || o[index_o + 1];

                return fio;
            END;
        $$
        LANGUAGE plpgsql;
    """)

    op.execute("""
        CREATE OR REPLACE FUNCTION random_dob() RETURNS DATE AS
        $$
            DECLARE
                year INT := 2000;
                month INT;
                day INT;
            BEGIN
                month := round(random()*11) + 1;
                day := round(random()*14) + 1;

                return make_date(year, month, day);
            END;
        $$
        LANGUAGE plpgsql;
    """)

    op.execute("""
        CREATE OR REPLACE FUNCTION random_sex() RETURNS TEXT AS
        $$
            DECLARE
                index_sex INT;
                sex TEXT[] := '{"Male", "Female"}';
            BEGIN
                index_sex := round(random());
                return sex[index_sex + 1];
            END;
        $$
        LANGUAGE plpgsql;
    """)
    # ###


def downgrade() -> None:
    # ###
    op.execute('DROP FUNCTION random_sex;')
    op.execute('DROP FUNCTION random_dob;')
    op.execute('DROP FUNCTION random_fio;')
    # ###
