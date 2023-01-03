"""added flag

Revision ID: 53bf58341d01
Revises: c24691a10669
Create Date: 2022-11-02 20:24:51.194423

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '53bf58341d01'
down_revision = 'c24691a10669'
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('Clubs', sa.Column('country_flag', sa.String(length=255), nullable=True))
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('Clubs', 'country_flag')
    # ### end Alembic commands ###
