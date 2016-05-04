"""empty message

Revision ID: 0d37ede16413
Revises: f076fb1ac986
Create Date: 2016-04-05 10:39:28.021664

"""

# revision identifiers, used by Alembic.
revision = '0d37ede16413'
down_revision = 'f076fb1ac986'

from alembic import op
import sqlalchemy as sa


def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.add_column('concert_info', sa.Column('genre', sa.String(length=1024), nullable=True))
    ### end Alembic commands ###


def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('concert_info', 'genre')
    ### end Alembic commands ###
