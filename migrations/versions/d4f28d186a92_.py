"""empty message

Revision ID: d4f28d186a92
Revises: d627a24313a4
Create Date: 2020-05-31 14:31:45.301336

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'd4f28d186a92'
down_revision = 'd627a24313a4'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('dishes', 'ingredients',
               existing_type=sa.VARCHAR(),
               nullable=False)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('dishes', 'ingredients',
               existing_type=sa.VARCHAR(),
               nullable=True)
    # ### end Alembic commands ###
