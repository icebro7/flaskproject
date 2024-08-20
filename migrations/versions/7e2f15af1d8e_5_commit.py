"""5 commit

Revision ID: 7e2f15af1d8e
Revises: 0947f6a6068a
Create Date: 2022-09-22 10:30:09.318683

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = '7e2f15af1d8e'
down_revision = '0947f6a6068a'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('user', 'password')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('user', sa.Column('password', mysql.VARCHAR(length=64), nullable=False))
    # ### end Alembic commands ###
