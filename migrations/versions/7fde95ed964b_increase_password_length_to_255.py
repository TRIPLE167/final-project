"""Increase password length to 255

Revision ID: 7fde95ed964b
Revises: 
Create Date: 2024-06-28 17:22:05.907436

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '7fde95ed964b'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('users')
    op.drop_table('UI')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('UI',
    sa.Column('email', sa.TEXT(), autoincrement=False, nullable=True),
    sa.Column('password', sa.TEXT(), autoincrement=False, nullable=True),
    sa.Column('name', sa.TEXT(), autoincrement=False, nullable=True),
    sa.Column('lastname', sa.TEXT(), autoincrement=False, nullable=True)
    )
    op.create_table('users',
    sa.Column('id', sa.INTEGER(), autoincrement=True, nullable=False),
    sa.Column('name', sa.VARCHAR(length=150), autoincrement=False, nullable=False),
    sa.Column('lastname', sa.VARCHAR(length=150), autoincrement=False, nullable=False),
    sa.Column('email', sa.VARCHAR(length=150), autoincrement=False, nullable=False),
    sa.Column('password', sa.VARCHAR(length=150), autoincrement=False, nullable=False),
    sa.PrimaryKeyConstraint('id', name='users_pkey'),
    sa.UniqueConstraint('email', name='users_email_key')
    )
    # ### end Alembic commands ###
