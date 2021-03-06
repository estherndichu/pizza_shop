"""Initial Migration

Revision ID: a8ebf051ea8a
Revises: 5b158ea06ec0
Create Date: 2021-03-05 14:33:56.497401

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'a8ebf051ea8a'
down_revision = '5b158ea06ec0'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('pizzas',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(), nullable=True),
    sa.Column('pic_path', sa.String(), nullable=True),
    sa.Column('size', sa.String(), nullable=True),
    sa.Column('price', sa.Integer(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.drop_table('pizza')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('pizza',
    sa.Column('id', sa.INTEGER(), autoincrement=True, nullable=False),
    sa.Column('name', sa.VARCHAR(), autoincrement=False, nullable=True),
    sa.Column('price', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('size', sa.VARCHAR(), autoincrement=False, nullable=True),
    sa.Column('pic_path', sa.VARCHAR(), autoincrement=False, nullable=True),
    sa.PrimaryKeyConstraint('id', name='pizza_pkey')
    )
    op.drop_table('pizzas')
    # ### end Alembic commands ###
