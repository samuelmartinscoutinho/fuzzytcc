"""Adicionado coluna operador na Tabela Regra

Revision ID: 009a2ffab446
Revises: f1ed7d199c24
Create Date: 2023-02-20 17:24:29.241451

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '009a2ffab446'
down_revision = 'f1ed7d199c24'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('regra', schema=None) as batch_op:
        batch_op.add_column(sa.Column('operador', sa.String(), nullable=True))

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('regra', schema=None) as batch_op:
        batch_op.drop_column('operador')

    # ### end Alembic commands ###