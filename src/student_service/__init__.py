from __future__ import annotations

import asyncpg
import os
from fastapi import HTTPException

async def get_student_profile(student_id: int) -> dict[str, str | int | list[str]]:
    """Retrieve student profile data by student ID."""

    database_url = os.getenv("DATABASE_URL")
    if not database_url:
        raise HTTPException(status_code=500, detail="Database URL not configured.")

    # Setup connection pool and query database
    try:
        async with asyncpg.create_pool(database_url) as pool:
            async with pool.acquire() as connection:

                query = "SELECT id, name, age FROM students WHERE id = $1;"
                student_data = await connection.fetchrow(query, student_id)

                if not student_data:
                    raise HTTPException(status_code=404, detail="Student profile not found.")

                courses_query = "SELECT course_name FROM student_courses WHERE student_id = $1;"
                student_courses = await connection.fetch(courses_query, student_id)

                return {
                    "id": student_data["id"],
                    "name": student_data["name"],
                    "age": student_data["age"],
                    "courses": [course["course_name"] for course in student_courses],
                }

    except asyncpg.PostgresError as err:
        raise HTTPException(status_code=500, detail="Database query failed.") from err

    except Exception as err:
        raise HTTPException(status_code=500, detail="Unknown error occurred.") from err
