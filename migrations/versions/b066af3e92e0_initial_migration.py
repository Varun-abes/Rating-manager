"""Initial migration.

Revision ID: b066af3e92e0
Revises: 
Create Date: 2022-11-20 02:05:37.564167

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'b066af3e92e0'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('feedback',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('customer', sa.String(length=100), nullable=True),
    sa.Column('seller', sa.String(length=100), nullable=True),
    sa.Column('rate', sa.Integer(), nullable=True),
    sa.Column('comment', sa.Text(), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('customer')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('feedback')
    # ### end Alembic commands ###