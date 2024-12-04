"""added_seller_info

Revision ID: 4d7764871e1b
Revises: a6ef5dab37cc
Create Date: 2024-12-04 22:08:27.696033

"""
from alembic import op
import sqlalchemy as sa

# revision identifiers, used by Alembic.
revision = '4d7764871e1b'
down_revision = 'a6ef5dab37cc'
branch_labels = None
depends_on = None


def upgrade():
    op.add_column('apartments', sa.Column('fio', sa.String(), nullable=True))
    op.add_column('apartments', sa.Column('phone', sa.String(), nullable=True))
    op.add_column('apartments', sa.Column('email', sa.String(), nullable=True))


def downgrade():
    op.drop_column('apartments', 'fio')
    op.drop_column('apartments', 'phone')
    op.drop_column('apartments', 'email')
