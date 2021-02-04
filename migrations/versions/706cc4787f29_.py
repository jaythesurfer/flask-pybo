"""empty message

Revision ID: 706cc4787f29
Revises: 2f9d22deb28e
Create Date: 2021-01-20 11:25:14.266096

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '706cc4787f29'
down_revision = '2f9d22deb28e'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('answer', schema=None) as batch_op:
        batch_op.alter_column('user_id',
               existing_type=sa.INTEGER(),
               nullable=False,
               existing_server_default=sa.text("'1'"))

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('answer', schema=None) as batch_op:
        batch_op.alter_column('user_id',
               existing_type=sa.INTEGER(),
               nullable=True,
               existing_server_default=sa.text("'1'"))

    # ### end Alembic commands ###