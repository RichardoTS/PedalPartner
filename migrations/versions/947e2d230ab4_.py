"""empty message

Revision ID: 947e2d230ab4
Revises: d7da08275f4c
Create Date: 2023-05-08 17:55:11.578002

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '947e2d230ab4'
down_revision = 'd7da08275f4c'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('users', schema=None) as batch_op:
        batch_op.alter_column('roles_id',
               existing_type=sa.INTEGER(),
               nullable=True)

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('users', schema=None) as batch_op:
        batch_op.alter_column('roles_id',
               existing_type=sa.INTEGER(),
               nullable=False)

    # ### end Alembic commands ###
