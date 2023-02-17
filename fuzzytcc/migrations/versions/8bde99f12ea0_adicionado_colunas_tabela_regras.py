"""Adicionado colunas tabela regras

Revision ID: 8bde99f12ea0
Revises: 5c50fb06b698
Create Date: 2023-02-17 14:07:38.699123

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '8bde99f12ea0'
down_revision = '5c50fb06b698'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('regra', schema=None) as batch_op:
        batch_op.add_column(sa.Column('imc_baixo', sa.Boolean(), nullable=True))
        batch_op.add_column(sa.Column('imc_medio', sa.Boolean(), nullable=True))
        batch_op.add_column(sa.Column('imc_alto', sa.Boolean(), nullable=True))
        batch_op.add_column(sa.Column('percentual_gordura_baixo', sa.Boolean(), nullable=True))
        batch_op.add_column(sa.Column('percentual_gordura_medio', sa.Boolean(), nullable=True))
        batch_op.add_column(sa.Column('percentual_gordura_alto', sa.Boolean(), nullable=True))
        batch_op.add_column(sa.Column('percentual_massa_baixo', sa.Boolean(), nullable=True))
        batch_op.add_column(sa.Column('percentual_massa_medio', sa.Boolean(), nullable=True))
        batch_op.add_column(sa.Column('percentual_massa_alto', sa.Boolean(), nullable=True))
        batch_op.drop_column('percentual_gordura')
        batch_op.drop_column('percentual_massa')
        batch_op.drop_column('imc')

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('regra', schema=None) as batch_op:
        batch_op.add_column(sa.Column('imc', sa.BOOLEAN(), autoincrement=False, nullable=True))
        batch_op.add_column(sa.Column('percentual_massa', sa.BOOLEAN(), autoincrement=False, nullable=True))
        batch_op.add_column(sa.Column('percentual_gordura', sa.BOOLEAN(), autoincrement=False, nullable=True))
        batch_op.drop_column('percentual_massa_alto')
        batch_op.drop_column('percentual_massa_medio')
        batch_op.drop_column('percentual_massa_baixo')
        batch_op.drop_column('percentual_gordura_alto')
        batch_op.drop_column('percentual_gordura_medio')
        batch_op.drop_column('percentual_gordura_baixo')
        batch_op.drop_column('imc_alto')
        batch_op.drop_column('imc_medio')
        batch_op.drop_column('imc_baixo')

    # ### end Alembic commands ###
