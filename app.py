from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from routers.news import router as news_router
from routers.health import router as health_router

app = FastAPI(
    title="LMS Core API",
    description="Learning Management System Core API",
    version="1.0.0"
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(news_router)
app.include_router(health_router)
