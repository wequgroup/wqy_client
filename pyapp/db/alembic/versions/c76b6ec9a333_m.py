"""${m}

Revision ID: c76b6ec9a333
Revises: 
Create Date: 2023-04-22 19:14:51.633955

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'c76b6ec9a333'
down_revision = None
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('device',
    sa.Column('device_id', sa.String(), nullable=False),
    sa.Column('device_password', sa.String(), server_default='', nullable=False),
    sa.Column('device_name', sa.String(), server_default='', nullable=False),
    sa.Column('auto_online', sa.String(), server_default='', nullable=False),
    sa.PrimaryKeyConstraint('device_id')
    )
    op.create_table('record',
    sa.Column('record_id', sa.String(), nullable=False),
    sa.Column('record_content', sa.String(), server_default='', nullable=False),
    sa.Column('record_name', sa.String(), server_default='', nullable=False),
    sa.PrimaryKeyConstraint('record_id')
    )
    op.create_table('storage_var',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('key', sa.String(), nullable=False),
    sa.Column('value', sa.String(), server_default='', nullable=False),
    sa.Column('remark', sa.String(), server_default='', nullable=False),
    sa.Column('created_at', sa.DateTime(), server_default=sa.text('(CURRENT_TIMESTAMP)'), nullable=True, comment='创建时间'),
    sa.Column('updated_at', sa.DateTime(), server_default=sa.text('(CURRENT_TIMESTAMP)'), nullable=True, comment='更新时间'),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_storage_var_key'), 'storage_var', ['key'], unique=False)
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_storage_var_key'), table_name='storage_var')
    op.drop_table('storage_var')
    op.drop_table('record')
    op.drop_table('device')
    # ### end Alembic commands ###
