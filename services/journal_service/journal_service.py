from fastapi import HTTPException, status
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import joinedload
from models.journal_model import Journal
from models.teacher_model import Teachers
from models.group_model import Groups
from models.subject_model import Subjects
from models.student_model import Students
from models.teacher_subject import TeacherSubject
from models.grade_model import Grade
from schemas.journals import JournalFullResponse, JournalListResponse, \
    LessonResponse, GroupShort, SubjectShort, TeacherShort, StudentShort
from schemas.grades import GradeResponse


class JournalService:

    @staticmethod
    async def create_journal(
            db: AsyncSession,
            group_id: int,
            subject_id: int,
            teacher_id: int,
            assistant_id: int | None = None,
    ) -> Journal:
        group = await db.get(Groups, group_id)
        if group is None:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                                detail="Group not found")

        subject = await db.get(Subjects, subject_id)
        if subject is None:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                                detail="Subject not found")

        teacher = await db.get(Teachers, teacher_id)
        if teacher is None:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                                detail="Teacher not found")

        ts_res = await db.execute(
            select(TeacherSubject).where(
                TeacherSubject.teacher_id == teacher_id,
                TeacherSubject.subject_id == subject_id,
            )
        )
        if ts_res.scalar_one_or_none() is None:
            raise HTTPException(
                status_code=status.HTTP_403_FORBIDDEN,
                detail="Teacher is not assigned to this subject",
            )

        if assistant_id is not None:
            assistant = await db.get(Teachers, assistant_id)
            if assistant is None:
                raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                                    detail="Assistant not found")

        existing = await db.execute(
            select(Journal).where(
                Journal.group_id == group_id,
                Journal.subject_id == subject_id,
            )
        )
        if existing.scalar_one_or_none() is not None:
            raise HTTPException(
                status_code=status.HTTP_409_CONFLICT,
                detail="Journal for this group and subject already exists",
            )

        journal = Journal(
            group_id=group_id,
            subject_id=subject_id,
            teacher_id=teacher_id,
            assistant_id=assistant_id,
        )
        db.add(journal)
        await db.commit()
        await db.refresh(journal)
        return journal

    @staticmethod
    async def get_journals(db: AsyncSession):
        result = await db.execute(
            select(Journal).options(
                joinedload(Journal.subject),
                joinedload(Journal.group)
            )
        )
        journals = result.unique().scalars().all()

        grouped = {}
        for journal in journals:
            subject_name = journal.subject.name
            if subject_name not in grouped:
                grouped[subject_name] = []
            group = journal.group
            grouped[subject_name].append({
                "id": group.id,
                "name": group.name,
                "course_number": group.course_number,
            })

        return [
            {"subject": subject, "groups": groups}
            for subject, groups in grouped.items()
        ]

    @staticmethod
    async def get_journal_by_id(db: AsyncSession,
                                journal_id: int) -> JournalFullResponse:
        journal = await db.get(Journal, journal_id)
        if journal is None:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                                detail="Journal not found")

        students_res = await db.execute(
            select(Students)
            .where(Students.group_id == journal.group_id)
            .order_by(Students.name)
        )
        students = students_res.scalars().all()

        lesson_ids = [l.id for l in journal.lessons]
        grades = []
        if lesson_ids:
            grades_res = await db.execute(
                select(Grade).where(Grade.lesson_id.in_(lesson_ids))
            )
            grades = grades_res.scalars().all()

        return JournalFullResponse(
            id=journal.id,
            group=GroupShort(id=journal.group.id, name=journal.group.name,
                             course_number=journal.group.course_number),
            subject=SubjectShort(id=journal.subject.id,
                                 name=journal.subject.name),
            teacher=TeacherShort(id=journal.teacher.id,
                                 name=journal.teacher.name),
            assistant=TeacherShort(id=journal.assistant.id,
                                   name=journal.assistant.name) if journal.assistant else None,
            lessons=[
                LessonResponse(
                    id=l.id,
                    date=l.date,
                    lesson_type=l.lesson_type,
                    order_index=l.order_index,
                    topic=l.topic,
                )
                for l in sorted(journal.lessons, key=lambda x: x.order_index)
            ],
            students=[StudentShort(id=s.id, name=s.name) for s in students],
            grades=[
                GradeResponse(
                    id=g.id,
                    lesson_id=g.lesson_id,
                    student_id=g.student_id,
                    value=g.value,
                    remark=g.remark,
                )
                for g in grades
            ],
        )

    @staticmethod
    async def delete_journal(db: AsyncSession, journal_id: int) -> None:
        journal = await db.get(Journal, journal_id)
        if journal is None:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                                detail="Journal not found")
        await db.delete(journal)
        await db.commit()


journal_service = JournalService()
