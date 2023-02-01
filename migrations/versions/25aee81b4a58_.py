"""empty message

Revision ID: 25aee81b4a58
Revises: 
Create Date: 2023-01-31 16:23:39.033659

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '25aee81b4a58'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('fountains',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('latitude', sa.Float(), nullable=False),
    sa.Column('longitude', sa.Float(), nullable=False),
    sa.Column('name', sa.String(), nullable=False),
    sa.Column('details', sa.String(), nullable=False),
    sa.Column('borough', sa.String(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('fountains')
    # ### end Alembic commands ###
