# LMS Core API

Learning Management System Core API - Backend system for education management based on FastAPI and PostgreSQL.

## 📋 Description

LMS Core API is a RESTful API for a learning management system that provides functionality for managing users, students, teachers, groups, subjects, journals, lessons, grades, and news. The system supports user roles, JWT authentication, and has a modular architecture.

## 🚀 Key Features

- **Authentication and Authorization**
  - JWT tokens (Access and Refresh)
  - User registration and login
  - Role-based system (Admin, Teacher, Student)
  - CAPTCHA verification during registration

- **User Management**
  - Administrators
  - Teachers (with group and subject assignments)
  - Students
  - Groups (with course number validation 1–6)

- **Educational Content**
  - Subject management
  - Teacher–Subject assignments (many-to-many)
  - Teacher–Group assignments (many-to-many)
  - News (with parsing from external sources)

- **Journal System** _(new)_
  - Journals linking a group, subject, and teacher (with optional assistant)
  - Lessons within journals (with types: LESSON, КР, СР, СЕМ, ТЕМ)
  - Grades per student per lesson (upsert & bulk upsert)

- **Integration with Data Catalog MCP**
  - Information retrieved exclusively using the Data Catalog MCP tool, ensuring consistent and accurate data handling.
  - Open questions noted if needed information is unavailable.

- **Security**
  - Password hashing (passlib)
  - JWT tokens with expiration
  - CORS middleware
  - Role verification dependencies

## 🛠 Tech Stack

- **FastAPI** - modern web framework for building APIs
- **SQLAlchemy 2.0** - ORM for database operations
- **PostgreSQL** - relational database
- **asyncpg** - async PostgreSQL driver
- **Pydantic** - data validation
- **JWT** - token-based authentication
- **uvicorn** - ASGI server
- **Docker** - application containerization
- **BeautifulSoup4** - web scraping
- **Alembic** - database migrations

## 📁 Project Structure

```
lms-core-api/
├── app.py                  # Main application file
├── requirements.txt        # Project dependencies
├── Dockerfile             # Docker configuration
├── alembic.ini            # Alembic configuration
├── core/                  # Core configurations
│   ├── config.py         # Application settings
│   └── constants.py      # Constants & LessonType enum
├── db/                    # Database
│   ├── database.py       # Database connection
│   └── init_db.py        # Database initialization
├── models/                # SQLAlchemy models
│   ├── auth_model.py
│   ├── admin_model.py
│   ├── teacher_model.py   # includes teacher_groups M2M table
│   ├── student_model.py
│   ├── group_model.py
│   ├── subject_model.py
│   ├── teacher_subject.py # Teacher–Subject M2M
│   ├── journal_model.py   # Journal model
│   ├── lesson_model.py    # Lesson model
│   ├── grade_model.py     # Grade model
│   └── news_model.py
├── routers/               # API endpoints
│   ├── auth.py
│   ├── users.py
│   ├── admins.py
│   ├── teachers.py
│   ├── students.py
│   ├── groups.py
│   ├── subjects.py
│   ├── journals.py        # Journal endpoints
│   ├── lessons.py         # Lesson endpoints (nested under journals)
│   ├── grades.py          # Grade endpoints (nested under journals)
│   └── news.py
├── schemas/               # Pydantic schemas
│   ├── auth.py
│   ├── users.py
│   ├── admins.py
│   ├── teachers.py
│   ├── students.py
│   ├── groups.py
│   ├── subjects.py
│   ├── journals.py
│   ├── lessons.py
│   ├── grades.py
│   └── news.py
├── services/              # Business logic
│   ├── admin_service/
│   ├── teacher_service/
│   ├── student_service/
│   ├── user_service/
│   ├── group_service/
│   ├── subject_service/
│   ├── journal_service/   # Journal business logic
│   ├── lesson_service/    # Lesson business logic
│   ├── grade_service/     # Grade business logic
│   └── news_service/
├── dependencies/          # FastAPI dependencies
│   ├── current_user.py   # Get current user
│   └── require_roles.py  # Role verification
├── utils/                 # Utilities
│   ├── auth.py
│   ├── jwt.py
│   ├── security.py
│   └── extract_roles.py
└── tests/                 # Tests
    └── test_captcha_service.py
```

## ⚙️ Setup

Refer to the main setup descriptions.

---
