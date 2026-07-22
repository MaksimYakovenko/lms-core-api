import asyncio
import logging
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from contextlib import asynccontextmanager
from routers.news import router as news_router
from routers.auth import router as auth_router
from routers.users import router as users_router
from routers.teachers import router as teachers_router
from routers.admins import router as admins_router
from routers.students import router as students_router
from routers.groups import router as groups_router
from routers.subjects import router as subjects_router
from routers.journals import router as journals_router
from routers.lessons import router as lessons_router
from routers.grades import router as grades_router
from routers.total_count import router as total_count_router
from routers.appointments import router as appointments_router
from routers.classrooms import router as classrooms_router
from routers.health import router as health_router
from db.database import engine, Base

logger = logging.getLogger("uvicorn.error")

DB_CONNECT_RETRIES = 10
DB_CONNECT_DELAY_SECONDS = 2


async def wait_for_db():
    last_exc = None
    for attempt in range(1, DB_CONNECT_RETRIES + 1):
        try:
            async with engine.begin() as conn:
                await conn.run_sync(Base.metadata.create_all)
            logger.info(f"Database connection established on attempt {attempt}")
            return
        except (ConnectionRefusedError, OSError) as exc:
            last_exc = exc
            logger.warning(
                f"DB connection attempt {attempt}/{DB_CONNECT_RETRIES} failed: {exc}. "
                f"Retrying in {DB_CONNECT_DELAY_SECONDS}s..."
            )
            await asyncio.sleep(DB_CONNECT_DELAY_SECONDS)
    logger.error("Could not connect to database after all retries")
    raise last_exc


@asynccontextmanager
async def lifespan(app: FastAPI):
    await wait_for_db()
    yield
    await engine.dispose()


app = FastAPI(
    title="LMS Core API",
    description="Learning Management System Core API",
    version="1.0.0",
    lifespan=lifespan
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(auth_router)
app.include_router(appointments_router)
app.include_router(news_router)
app.include_router(users_router)
app.include_router(admins_router)
app.include_router(teachers_router)
app.include_router(students_router)
app.include_router(groups_router)
app.include_router(subjects_router)
app.include_router(classrooms_router)
app.include_router(journals_router)
app.include_router(lessons_router)
app.include_router(grades_router)
app.include_router(total_count_router)
app.include_router(health_router)