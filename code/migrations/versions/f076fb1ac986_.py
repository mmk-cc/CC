"""empty message

Revision ID: f076fb1ac986
Revises: None
Create Date: 2016-04-03 21:42:30.394872

"""

# revision identifiers, used by Alembic.
revision = 'f076fb1ac986'
down_revision = None

from alembic import op
import sqlalchemy as sa


def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.create_table('concert_info',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('mainArtist', sa.String(length=1024), nullable=True),
    sa.Column('instrument', sa.String(length=1024), nullable=True),
    sa.Column('accompanyingArtists', sa.String(length=1024), nullable=True),
    sa.Column('festival', sa.String(length=1024), nullable=True),
    sa.Column('timestamp', sa.DateTime(), nullable=True),
    sa.Column('auditorium', sa.String(length=1024), nullable=True),
    sa.Column('address', sa.String(length=1024), nullable=True),
    sa.Column('city', sa.String(length=1024), nullable=True),
    sa.Column('state', sa.String(length=1024), nullable=True),
    sa.Column('country', sa.String(length=1024), nullable=True),
    sa.Column('url', sa.String(length=1024), nullable=True),
    sa.Column('contactEmail', sa.String(length=1024), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    ### end Alembic commands ###


def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('concert_info')
    ### end Alembic commands ###
