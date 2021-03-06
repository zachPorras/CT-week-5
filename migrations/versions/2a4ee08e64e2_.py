"""empty message

Revision ID: 2a4ee08e64e2
Revises: 
Create Date: 2021-08-05 19:02:36.702505

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '2a4ee08e64e2'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('user',
    sa.Column('id', sa.String(), nullable=False),
    sa.Column('email', sa.String(length=150), nullable=False),
    sa.Column('password', sa.String(), nullable=False),
    sa.Column('token', sa.String(), nullable=True),
    sa.Column('date_created', sa.DateTime(), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('email'),
    sa.UniqueConstraint('token')
    )
    op.create_table('hike',
    sa.Column('id', sa.String(), nullable=False),
    sa.Column('hike_name', sa.String(length=150), nullable=True),
    sa.Column('country', sa.String(length=100), nullable=True),
    sa.Column('district', sa.String(length=100), nullable=True),
    sa.Column('city', sa.String(length=100), nullable=True),
    sa.Column('coordinates', sa.String(length=30), nullable=True),
    sa.Column('length', sa.Numeric(precision=6, scale=2), nullable=True),
    sa.Column('elevation_gain', sa.Numeric(precision=5, scale=0), nullable=True),
    sa.Column('hike_type', sa.String(length=50), nullable=True),
    sa.Column('difficulty', sa.String(length=30), nullable=True),
    sa.Column('parking', sa.Boolean(), nullable=True),
    sa.Column('user_token', sa.String(), nullable=False),
    sa.ForeignKeyConstraint(['user_token'], ['user.token'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('hike')
    op.drop_table('user')
    # ### end Alembic commands ###
