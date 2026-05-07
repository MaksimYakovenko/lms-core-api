"""add title and description to lessons

Revision ID: 83dcfcc364a6
Revises: a1b2c3d4e5f6
Create Date: 2026-05-07 22:56:02.647048

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '83dcfcc364a6'
down_revision: Union[str, None] = 'a1b2c3d4e5f6'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.add_column('lessons', sa.Column('title', sa.String(length=500), nullable=True))
    op.add_column('lessons', sa.Column('description', sa.Text(), nullable=True))


def downgrade() -> None:
    op.drop_column('lessons', 'description')
    op.drop_column('lessons', 'title')


def _unused_downgrade() -> None:
    op.create_table('journals',
    sa.Column('id', sa.INTEGER(), server_default=sa.text("nextval('journals_id_seq'::regclass)"), autoincrement=True, nullable=False),
    sa.Column('group_id', sa.INTEGER(), autoincrement=False, nullable=False),
    sa.Column('subject_id', sa.INTEGER(), autoincrement=False, nullable=False),
    sa.Column('teacher_id', sa.INTEGER(), autoincrement=False, nullable=False),
    sa.Column('assistant_id', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.ForeignKeyConstraint(['assistant_id'], ['teachers.id'], name='journals_assistant_id_fkey', ondelete='SET NULL'),
    sa.ForeignKeyConstraint(['group_id'], ['groups.id'], name='journals_group_id_fkey', ondelete='CASCADE'),
    sa.ForeignKeyConstraint(['subject_id'], ['subjects.id'], name='journals_subject_id_fkey', ondelete='CASCADE'),
    sa.ForeignKeyConstraint(['teacher_id'], ['teachers.id'], name='journals_teacher_id_fkey', ondelete='CASCADE'),
    sa.PrimaryKeyConstraint('id', name='journals_pkey'),
    sa.UniqueConstraint('group_id', 'subject_id', name='uq_journal_group_subject'),
    postgresql_ignore_search_path=False
    )
    op.create_index('ix_journals_id', 'journals', ['id'], unique=False)
    op.create_table('classrooms',
    sa.Column('id', sa.INTEGER(), server_default=sa.text("nextval('classrooms_id_seq'::regclass)"), autoincrement=True, nullable=False),
    sa.Column('name', sa.VARCHAR(length=100), autoincrement=False, nullable=False),
    sa.PrimaryKeyConstraint('id', name='classrooms_pkey'),
    sa.UniqueConstraint('name', name='classrooms_name_key'),
    postgresql_ignore_search_path=False
    )
    op.create_index('ix_classrooms_id', 'classrooms', ['id'], unique=False)
    op.create_table('subjects',
    sa.Column('id', sa.INTEGER(), server_default=sa.text("nextval('subjects_id_seq'::regclass)"), autoincrement=True, nullable=False),
    sa.Column('name', sa.VARCHAR(length=150), autoincrement=False, nullable=False),
    sa.PrimaryKeyConstraint('id', name='subjects_pkey'),
    postgresql_ignore_search_path=False
    )
    op.create_index('ix_subjects_name', 'subjects', ['name'], unique=True)
    op.create_index('ix_subjects_id', 'subjects', ['id'], unique=False)
    op.create_table('teacher_subject',
    sa.Column('id', sa.INTEGER(), autoincrement=True, nullable=False),
    sa.Column('teacher_id', sa.INTEGER(), autoincrement=False, nullable=False),
    sa.Column('subject_id', sa.INTEGER(), autoincrement=False, nullable=False),
    sa.ForeignKeyConstraint(['subject_id'], ['subjects.id'], name='teacher_subject_subject_id_fkey', ondelete='CASCADE'),
    sa.ForeignKeyConstraint(['teacher_id'], ['teachers.id'], name='teacher_subject_teacher_id_fkey', ondelete='CASCADE'),
    sa.PrimaryKeyConstraint('id', name='teacher_subject_pkey'),
    sa.UniqueConstraint('teacher_id', 'subject_id', name='uq_teacher_subject')
    )
    op.create_index('ix_teacher_subject_id', 'teacher_subject', ['id'], unique=False)
    op.create_table('lessons',
    sa.Column('id', sa.INTEGER(), server_default=sa.text("nextval('lessons_id_seq'::regclass)"), autoincrement=True, nullable=False),
    sa.Column('journal_id', sa.INTEGER(), autoincrement=False, nullable=False),
    sa.Column('date', sa.DATE(), autoincrement=False, nullable=False),
    sa.Column('lesson_type', sa.VARCHAR(length=20), autoincrement=False, nullable=False),
    sa.Column('order_index', sa.INTEGER(), autoincrement=False, nullable=False),
    sa.Column('topic', sa.VARCHAR(length=500), autoincrement=False, nullable=True),
    sa.Column('lesson_number', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('classroom_id', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.ForeignKeyConstraint(['classroom_id'], ['classrooms.id'], name='lessons_classroom_id_fkey', ondelete='SET NULL'),
    sa.ForeignKeyConstraint(['journal_id'], ['journals.id'], name='lessons_journal_id_fkey', ondelete='CASCADE'),
    sa.PrimaryKeyConstraint('id', name='lessons_pkey'),
    postgresql_ignore_search_path=False
    )
    op.create_index('ix_lessons_id', 'lessons', ['id'], unique=False)
    op.create_table('grades',
    sa.Column('id', sa.INTEGER(), autoincrement=True, nullable=False),
    sa.Column('lesson_id', sa.INTEGER(), autoincrement=False, nullable=False),
    sa.Column('student_id', sa.INTEGER(), autoincrement=False, nullable=False),
    sa.Column('value', sa.VARCHAR(length=20), autoincrement=False, nullable=True),
    sa.Column('remark', sa.VARCHAR(length=500), autoincrement=False, nullable=True),
    sa.ForeignKeyConstraint(['lesson_id'], ['lessons.id'], name='grades_lesson_id_fkey', ondelete='CASCADE'),
    sa.ForeignKeyConstraint(['student_id'], ['students.id'], name='grades_student_id_fkey', ondelete='CASCADE'),
    sa.PrimaryKeyConstraint('id', name='grades_pkey'),
    sa.UniqueConstraint('lesson_id', 'student_id', name='uq_grade_lesson_student')
    )
    op.create_index('ix_grades_id', 'grades', ['id'], unique=False)
    # ### end Alembic commands ###
