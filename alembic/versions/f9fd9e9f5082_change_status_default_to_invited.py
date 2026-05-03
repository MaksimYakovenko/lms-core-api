"""change_status_default_to_invited

Revision ID: f9fd9e9f5082
Revises: 506059b36373
Create Date: 2026-04-26 13:19:39.426494

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'f9fd9e9f5082'
down_revision: Union[str, None] = '506059b36373'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.alter_column('teachers', 'status', server_default='INVITED')
    op.alter_column('admins', 'status', server_default='INVITED')
    op.alter_column('students', 'status', server_default='INVITED')


def downgrade() -> None:
    op.alter_column('teachers', 'status', server_default='ACTIVE')
    op.alter_column('admins', 'status', server_default='ACTIVE')
    op.alter_column('students', 'status', server_default='ACTIVE')
