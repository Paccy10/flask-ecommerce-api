"""empty message

Revision ID: 68aab11ca8ad
Revises: c5cec0a4ee8c
Create Date: 2019-11-28 12:37:57.515648

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '68aab11ca8ad'
down_revision = 'c5cec0a4ee8c'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('carts',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('created_at', sa.DateTime(), nullable=True),
    sa.Column('updated_at', sa.DateTime(), nullable=True),
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('user_id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('carts')
    # ### end Alembic commands ###
