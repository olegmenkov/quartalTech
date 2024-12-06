"""added new columns to apartments

Revision ID: a6ef5dab37cc
Revises: df343561efcc
Create Date: 2024-12-03 21:47:28.221765

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'a6ef5dab37cc'
down_revision = 'df343561efcc'
branch_labels = None
depends_on = None


def upgrade():
    op.add_column('apartments', sa.Column('floor', sa.Integer(), nullable=False))
    op.add_column('apartments', sa.Column('total_floors', sa.Integer(), nullable=False))
    op.add_column('apartments', sa.Column('district', sa.String(), nullable=True))
    op.add_column('apartments', sa.Column('underground', sa.String(), nullable=True))


def downgrade():
    op.drop_column('apartments', 'floor')
    op.drop_column('apartments', 'total_floors')
    op.drop_column('apartments', 'district')
    op.drop_column('apartments', 'underground')
