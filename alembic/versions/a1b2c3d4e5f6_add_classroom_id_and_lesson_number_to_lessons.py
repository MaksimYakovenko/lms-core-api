"""add_classroom_id_and_lesson_number_to_lessons

Revision ID: a1b2c3d4e5f6
Revises: f9fd9e9f5082
Create Date: 2026-05-04 00:10:00.000000

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'a1b2c3d4e5f6'
down_revision: Union[str, None] = 'f9fd9e9f5082'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.add_column('lessons', sa.Column('lesson_number', sa.Integer(), nullable=True))
    op.add_column('lessons', sa.Column('classroom_id', sa.Integer(), nullable=True))
    op.create_foreign_key(
        'lessons_classroom_id_fkey',
        'lessons', 'classrooms',
        ['classroom_id'], ['id'],
        ondelete='SET NULL'
    )
    op.alter_column('lessons', 'lesson_type', type_=sa.String(length=20))


def downgrade() -> None:
    op.drop_constraint('lessons_classroom_id_fkey', 'lessons', type_='foreignkey')
    op.drop_column('lessons', 'classroom_id')
    op.drop_column('lessons', 'lesson_number')
    op.alter_column('lessons', 'lesson_type', type_=sa.String(length=10))
