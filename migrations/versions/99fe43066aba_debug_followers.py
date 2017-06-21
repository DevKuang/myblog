"""debug followers

Revision ID: 99fe43066aba
Revises: 24c720bfcdf2
Create Date: 2017-06-20 18:33:20.488559

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '99fe43066aba'
down_revision = '24c720bfcdf2'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('posts', sa.Column('body_html', sa.Text(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('posts', 'body_html')
    # ### end Alembic commands ###
