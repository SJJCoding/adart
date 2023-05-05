"""Add column anno_file_name to Task model

Revision ID: 1e4de8589b40
Revises: 5da4cd60022b
Create Date: 2021-12-01 05:39:29.315388

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '1e4de8589b40'
down_revision = '5da4cd60022b'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('task', sa.Column('anno_file_name', sa.String(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('task', 'anno_file_name')
    # ### end Alembic commands ###