"""5 commit

Revision ID: 725fd95aefb1
Revises: 7db64b64e500
Create Date: 2022-09-23 15:30:46.283426

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '725fd95aefb1'
down_revision = '7db64b64e500'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('code',
    sa.Column('phonecode', sa.String(length=6), nullable=False),
    sa.Column('sendTime', sa.DateTime(), nullable=True),
    sa.PrimaryKeyConstraint('phonecode')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('code')
    # ### end Alembic commands ###
