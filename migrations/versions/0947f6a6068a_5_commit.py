"""5 commit

Revision ID: 0947f6a6068a
Revises: 91d1563a4095
Create Date: 2022-09-22 10:25:57.624679

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '0947f6a6068a'
down_revision = '91d1563a4095'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('user', sa.Column('phonecode', sa.String(length=6), nullable=False))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('user', 'phonecode')
    # ### end Alembic commands ###
