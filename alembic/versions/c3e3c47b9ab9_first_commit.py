"""First commit

Revision ID: c3e3c47b9ab9
Revises: 2d96bf95e88b
Create Date: 2023-11-08 00:21:23.671429

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'c3e3c47b9ab9'
down_revision: Union[str, None] = '2d96bf95e88b'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('application',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=256), nullable=False),
    sa.Column('url', sa.String(length=256), nullable=True),
    sa.Column('is_active', sa.Boolean(), nullable=True),
    sa.Column('type_entity', sa.Integer(), nullable=True),
    sa.Column('time_created', sa.DateTime(timezone=True), server_default=sa.text('(CURRENT_TIMESTAMP)'), nullable=True),
    sa.Column('time_updated', sa.DateTime(timezone=True), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('name')
    )
    op.create_index(op.f('ix_application_id'), 'application', ['id'], unique=False)
    op.create_index(op.f('ix_application_type_entity'), 'application', ['type_entity'], unique=False)
    op.create_table('genero',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(), nullable=False),
    sa.Column('time_created', sa.DateTime(timezone=True), server_default=sa.text('(CURRENT_TIMESTAMP)'), nullable=True),
    sa.Column('time_updated', sa.DateTime(timezone=True), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_genero_id'), 'genero', ['id'], unique=False)
    op.create_index(op.f('ix_genero_name'), 'genero', ['name'], unique=True)
    op.create_table('organization',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=256), nullable=False),
    sa.Column('time_created', sa.DateTime(timezone=True), server_default=sa.text('(CURRENT_TIMESTAMP)'), nullable=True),
    sa.Column('time_updated', sa.DateTime(timezone=True), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('name')
    )
    op.create_index(op.f('ix_organization_id'), 'organization', ['id'], unique=False)
    op.create_table('sexo',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(), nullable=False),
    sa.Column('time_created', sa.DateTime(timezone=True), server_default=sa.text('(CURRENT_TIMESTAMP)'), nullable=True),
    sa.Column('time_updated', sa.DateTime(timezone=True), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_sexo_id'), 'sexo', ['id'], unique=False)
    op.create_index(op.f('ix_sexo_name'), 'sexo', ['name'], unique=True)
    op.create_table('permissions',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('label', sa.String(), nullable=False),
    sa.Column('name', sa.String(), nullable=False),
    sa.Column('is_system', sa.Boolean(), nullable=True),
    sa.Column('aplication_id', sa.Integer(), nullable=True),
    sa.Column('time_created', sa.DateTime(timezone=True), server_default=sa.text('(CURRENT_TIMESTAMP)'), nullable=True),
    sa.Column('time_updated', sa.DateTime(timezone=True), nullable=True),
    sa.ForeignKeyConstraint(['aplication_id'], ['application.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_permissions_id'), 'permissions', ['id'], unique=False)
    op.create_index(op.f('ix_permissions_name'), 'permissions', ['name'], unique=True)
    op.create_table('role',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(), nullable=False),
    sa.Column('aplication_id', sa.Integer(), nullable=False),
    sa.Column('time_created', sa.DateTime(timezone=True), server_default=sa.text('(CURRENT_TIMESTAMP)'), nullable=True),
    sa.Column('time_updated', sa.DateTime(timezone=True), nullable=True),
    sa.ForeignKeyConstraint(['aplication_id'], ['application.id'], ondelete='CASCADE', initially='DEFERRED', deferrable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_role_id'), 'role', ['id'], unique=False)
    op.create_index(op.f('ix_role_name'), 'role', ['name'], unique=True)
    op.create_table('user',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('organization_id', sa.Integer(), nullable=True),
    sa.Column('title', sa.String(), nullable=True),
    sa.Column('names', sa.String(), nullable=False),
    sa.Column('last_name', sa.String(), nullable=False),
    sa.Column('mother_last_name', sa.String(), nullable=True),
    sa.Column('genero_id', sa.Integer(), nullable=True),
    sa.Column('sexo_id', sa.Integer(), nullable=True),
    sa.Column('email', sa.String(), nullable=False),
    sa.Column('password', sa.String(), nullable=True),
    sa.Column('is_active', sa.Boolean(), nullable=True),
    sa.Column('birth_date', sa.Date(), nullable=True),
    sa.Column('phone_mobile', sa.String(length=20), nullable=True),
    sa.Column('avatar', sa.String(), nullable=True),
    sa.Column('time_created', sa.DateTime(timezone=True), server_default=sa.text('(CURRENT_TIMESTAMP)'), nullable=True),
    sa.Column('time_updated', sa.DateTime(timezone=True), nullable=True),
    sa.ForeignKeyConstraint(['genero_id'], ['genero.id'], initially='DEFERRED', deferrable=True),
    sa.ForeignKeyConstraint(['organization_id'], ['organization.id'], initially='DEFERRED', deferrable=True),
    sa.ForeignKeyConstraint(['sexo_id'], ['sexo.id'], initially='DEFERRED', deferrable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_user_email'), 'user', ['email'], unique=False)
    op.create_index(op.f('ix_user_id'), 'user', ['id'], unique=False)
    op.create_index(op.f('ix_user_last_name'), 'user', ['last_name'], unique=False)
    op.create_index(op.f('ix_user_names'), 'user', ['names'], unique=False)
    op.create_index(op.f('ix_user_organization_id'), 'user', ['organization_id'], unique=False)
    op.create_index(op.f('ix_user_title'), 'user', ['title'], unique=False)
    op.create_table('permissionsroles',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('role_id', sa.Integer(), nullable=True),
    sa.Column('permissions_id', sa.Integer(), nullable=True),
    sa.Column('time_created', sa.DateTime(timezone=True), server_default=sa.text('(CURRENT_TIMESTAMP)'), nullable=True),
    sa.Column('time_updated', sa.DateTime(timezone=True), nullable=True),
    sa.ForeignKeyConstraint(['permissions_id'], ['permissions.id'], ondelete='CASCADE'),
    sa.ForeignKeyConstraint(['role_id'], ['role.id'], ondelete='CASCADE'),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('role_id', 'permissions_id')
    )
    op.create_index(op.f('ix_permissionsroles_id'), 'permissionsroles', ['id'], unique=False)
    op.create_table('usersroles',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('role_id', sa.Integer(), nullable=True),
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.Column('time_created', sa.DateTime(timezone=True), server_default=sa.text('(CURRENT_TIMESTAMP)'), nullable=True),
    sa.Column('time_updated', sa.DateTime(timezone=True), nullable=True),
    sa.ForeignKeyConstraint(['role_id'], ['role.id'], ondelete='CASCADE'),
    sa.ForeignKeyConstraint(['user_id'], ['user.id'], ondelete='CASCADE'),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('role_id', 'user_id')
    )
    op.create_index(op.f('ix_usersroles_id'), 'usersroles', ['id'], unique=False)
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_usersroles_id'), table_name='usersroles')
    op.drop_table('usersroles')
    op.drop_index(op.f('ix_permissionsroles_id'), table_name='permissionsroles')
    op.drop_table('permissionsroles')
    op.drop_index(op.f('ix_user_title'), table_name='user')
    op.drop_index(op.f('ix_user_organization_id'), table_name='user')
    op.drop_index(op.f('ix_user_names'), table_name='user')
    op.drop_index(op.f('ix_user_last_name'), table_name='user')
    op.drop_index(op.f('ix_user_id'), table_name='user')
    op.drop_index(op.f('ix_user_email'), table_name='user')
    op.drop_table('user')
    op.drop_index(op.f('ix_role_name'), table_name='role')
    op.drop_index(op.f('ix_role_id'), table_name='role')
    op.drop_table('role')
    op.drop_index(op.f('ix_permissions_name'), table_name='permissions')
    op.drop_index(op.f('ix_permissions_id'), table_name='permissions')
    op.drop_table('permissions')
    op.drop_index(op.f('ix_sexo_name'), table_name='sexo')
    op.drop_index(op.f('ix_sexo_id'), table_name='sexo')
    op.drop_table('sexo')
    op.drop_index(op.f('ix_organization_id'), table_name='organization')
    op.drop_table('organization')
    op.drop_index(op.f('ix_genero_name'), table_name='genero')
    op.drop_index(op.f('ix_genero_id'), table_name='genero')
    op.drop_table('genero')
    op.drop_index(op.f('ix_application_type_entity'), table_name='application')
    op.drop_index(op.f('ix_application_id'), table_name='application')
    op.drop_table('application')
    # ### end Alembic commands ###
