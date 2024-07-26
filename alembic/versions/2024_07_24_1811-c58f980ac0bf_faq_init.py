"""faq init

Revision ID: c58f980ac0bf
Revises:
Create Date: 2024-07-24 18:11:20.274668

"""

import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

from alembic import op

# revision identifiers, used by Alembic.
revision = "c58f980ac0bf"
down_revision = None
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table(
        "faq",
        sa.Column("id", sa.Integer(), autoincrement=True, nullable=False),
        sa.Column("question", sa.Text(), nullable=False),
        sa.Column("complimentary", sa.Text(), nullable=True),
        sa.Column("answer", sa.Text(), nullable=False),
        sa.Column("language", sa.String(), nullable=True),
        sa.Column("url", sa.String(), nullable=True),
        sa.Column("category", sa.String(), nullable=True),
        sa.Column("keywords", sa.Text(), nullable=True),
        sa.Column("embedding", postgresql.ARRAY(sa.Float()), nullable=True),
        sa.PrimaryKeyConstraint("id"),
    )
    op.create_index(op.f("ix_faq_id"), "faq", ["id"], unique=False)
    op.create_index(op.f("ix_faq_question"), "faq", ["question"], unique=True)
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f("ix_faq_question"), table_name="faq")
    op.drop_index(op.f("ix_faq_id"), table_name="faq")
    op.drop_table("faq")
    # ### end Alembic commands ###
