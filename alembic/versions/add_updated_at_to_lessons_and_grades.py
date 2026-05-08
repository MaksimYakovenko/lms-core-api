"""add_updated_at_to_lessons_and_grades

Revision ID: c1d2e3f4a5b6
Revises: 83dcfcc364a6
Create Date: 2026-05-08

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


revision: str = 'b7c8d9e0f1a2'
down_revision: Union[str, None] = '83dcfcc364a6'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.add_column('lessons', sa.Column(
        'updated_at',
        sa.DateTime(timezone=True),
        server_default=sa.func.now(),
        nullable=False
    ))
    op.add_column('grades', sa.Column(
        'updated_at',
        sa.DateTime(timezone=True),
        server_default=sa.func.now(),
        nullable=False
    ))


def downgrade() -> None:
    op.drop_column('grades', 'updated_at')
    op.drop_column('lessons', 'updated_at')
