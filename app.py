from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from contextlib import asynccontextmanager
from routers.news import router as news_router
from routers.auth import router as auth_router
from routers.users import router as users_router
from routers.teachers import router as teachers_router
from routers.admins import router as admins_router
from db.database import engine, Base
from models.auth_model import User
from models.news_model import News
from models.admin_model import Admins
from models.teacher_model import Teachers


@asynccontextmanager
async def lifespan(app: FastAPI):
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)
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
app.include_router(news_router)
app.include_router(users_router)
app.include_router(admins_router)
app.include_router(teachers_router)
