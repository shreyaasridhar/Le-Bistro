"""empty message

Revision ID: d627a24313a4
Revises: 
Create Date: 2020-05-31 14:31:29.308892

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'd627a24313a4'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('dishes', 'ingredients',
               existing_type=sa.VARCHAR(),
               nullable=True)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('dishes', 'ingredients',
               existing_type=sa.VARCHAR(),
               nullable=False)
    # ### end Alembic commands ###
