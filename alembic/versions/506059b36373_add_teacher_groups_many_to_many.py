"""add_teacher_groups_many_to_many

Revision ID: 506059b36373
Revises: 
Create Date: 2026-04-02 20:12:22.484237

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '506059b36373'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # Додаємо відсутні колонки в таблицю teachers
    op.add_column('teachers', sa.Column('name', sa.String(100), nullable=True))
    op.add_column('teachers', sa.Column('role', sa.String(20), nullable=True))
    op.add_column('teachers', sa.Column('status', sa.String(20), server_default='ACTIVE', nullable=True))

    # Заповнюємо існуючі рядки дефолтними значеннями
    op.execute("UPDATE teachers SET name = 'Unregistered' WHERE name IS NULL")
    op.execute("UPDATE teachers SET role = 'TEACHER' WHERE role IS NULL")

    # Робимо колонки NOT NULL після заповнення
    op.alter_column('teachers', 'name', nullable=False)
    op.alter_column('teachers', 'role', nullable=False)

    # Видаляємо старий стовпець groups_id якщо він ще є
    conn = op.get_bind()
    inspector = sa.inspect(conn)
    columns = [c['name'] for c in inspector.get_columns('teachers')]
    if 'groups_id' in columns:
        op.drop_column('teachers', 'groups_id')


def downgrade() -> None:
    op.drop_column('teachers', 'status')
    op.drop_column('teachers', 'role')
    op.drop_column('teachers', 'name')
