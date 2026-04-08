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

## ⚙️ Installation and Setup

### Prerequisites

- Python 3.11+
- PostgreSQL 12+
- pip

### Local Installation

1. Clone the repository:
```bash
git clone <repository-url>
cd lms-core-api
```

2. Create a virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Create `.env` file in the root directory:
```env
# Database
DB_HOST=localhost
DB_PORT=5432
DB_NAME=lms_db
DB_USER=postgres
DB_PASSWORD=your_password

# JWT
SECRET_KEY=your-secret-key-here
ACCESS_TOKEN_EXPIRE_MINUTES=15
REFRESH_TOKEN_EXPIRE_DAYS=7
ALGORITHM=HS256
```

5. Apply database migrations:
```bash
alembic upgrade head
```

6. Start the server:
```bash
uvicorn app:app --reload --host 0.0.0.0 --port 8000
```

API will be available at: `http://localhost:8000`

API Documentation (Swagger): `http://localhost:8000/docs`

### Running with Docker

1. Build the Docker image:
```bash
docker build -t lms-core-api .
```

2. Run the container:
```bash
docker run -d \
  -p 8000:8000 \
  -e DB_HOST=your_db_host \
  -e DB_PORT=5432 \
  -e DB_NAME=lms_db \
  -e DB_USER=postgres \
  -e DB_PASSWORD=your_password \
  -e SECRET_KEY=your_secret_key \
  --name lms-api \
  lms-core-api
```

## 📚 API Endpoints

### Authentication
- `POST /auth/sign-up` - User registration
- `POST /auth/sign-in` - User login
- `POST /auth/refresh` - Refresh token
- `GET /auth/captcha` - Get CAPTCHA

### Users
- `GET /users` - List users
- `GET /users/me` - Get current user
- `PUT /users/{id}` - Update user
- `DELETE /users/{id}` - Delete user

### Administrators
- `GET /admins` - List administrators
- `POST /admins` - Create administrator
- `GET /admins/{id}` - Get administrator
- `PUT /admins/{id}` - Update administrator
- `DELETE /admins/{id}` - Delete administrator

### Teachers
- `GET /teachers/get_teachers` - List teachers
- `POST /teachers/create_teacher` - Create teacher
- `PUT /teachers/update_teacher/{id}` - Update teacher
- `DELETE /teachers/delete_teacher/{id}` - Delete teacher
- `PUT /teachers/assign_to_groups` - Assign teacher to groups (many-to-many)
- `POST /teachers/{teacher_id}/subjects` - Assign subject to teacher
- `DELETE /teachers/{teacher_id}/subjects/{subject_id}` - Remove subject from teacher
- `GET /teachers/{teacher_id}/subjects` - Get teacher's subjects

### Students
- `GET /students` - List students
- `POST /students` - Create student
- `GET /students/{id}` - Get student
- `PUT /students/{id}` - Update student
- `DELETE /students/{id}` - Delete student

### Groups
- `GET /groups/get_groups` - List groups
- `POST /groups/create_group` - Create group

### Subjects
- `GET /subjects` - List subjects
- `POST /subjects` - Create subject
- `GET /subjects/{id}` - Get subject
- `PUT /subjects/{id}` - Update subject
- `DELETE /subjects/{id}` - Delete subject

### Journals _(new)_
- `POST /journals` - Create journal
- `GET /journals` - List journals (filter by `group_id`, `teacher_id`)
- `GET /journals/{journal_id}` - Get journal with lessons and grades
- `DELETE /journals/{journal_id}` - Delete journal

### Lessons _(new)_
- `POST /journals/{journal_id}/lessons` - Add lesson to journal
- `GET /journals/{journal_id}/lessons` - List lessons in journal
- `PUT /journals/{journal_id}/lessons/{lesson_id}` - Update lesson
- `DELETE /journals/{journal_id}/lessons/{lesson_id}` - Delete lesson

### Grades _(new)_
- `PUT /journals/{journal_id}/grades` - Upsert a single grade
- `PUT /journals/{journal_id}/grades/bulk` - Bulk upsert grades
- `GET /journals/{journal_id}/grades` - Get all grades in journal
- `DELETE /journals/{journal_id}/grades/{grade_id}` - Delete grade

### News
- `GET /news` - List news
- `POST /news/parse` - Parse news
- `GET /news/{id}` - Get news item
- `DELETE /news/{id}` - Delete news item

## 📓 Lesson Types

Lessons support the following types (defined in `LessonType` enum):

| Code | Description |
|------|-------------|
| `LESSON` | Regular lesson |
| `КР` | Control work |
| `СР` | Independent work |
| `СЕМ` | Seminar |
| `ТЕМ` | Thematic evaluation |

## 🔐 Authentication

The API uses JWT tokens for authentication. After logging in, you will receive:
- `access_token` - short-lived token for API access (default 15 minutes)
- `refresh_token` - long-lived token for refreshing access token (default 7 days)

Use the access token in the request header:
```
Authorization: Bearer <access_token>
```

## 👥 User Roles

The system supports the following roles:
- **Admin** - full access to all features
- **Teacher** - access to journal, lesson, grade, and subject management
- **Student** - access to view information

## 🧪 Testing

Run tests:
```bash
pytest tests/
```

Run with code coverage:
```bash
pytest --cov=. tests/
```

## 🔧 Development

### Database Migrations

Create a new migration:
```bash
alembic revision --autogenerate -m "description"
```

Apply migrations:
```bash
alembic upgrade head
```

Rollback migration:
```bash
alembic downgrade -1
```

### Adding New Dependencies

After adding new dependencies, update requirements.txt:
```bash
pip freeze > requirements.txt
```

## 📝 Environment Variables

| Variable | Description | Default Value |
|---------|-------------|---------------|
| DB_HOST | Database host | localhost |
| DB_PORT | Database port | 5432 |
| DB_NAME | Database name | lms_db |
| DB_USER | Database user | postgres |
| DB_PASSWORD | Database password | postgres |
| SECRET_KEY | Secret key for JWT | - |
| ACCESS_TOKEN_EXPIRE_MINUTES | Access token lifetime | 15 |
| REFRESH_TOKEN_EXPIRE_DAYS | Refresh token lifetime | 7 |
| ALGORITHM | JWT encryption algorithm | HS256 |

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 📄 License

This project is distributed under the MIT License.

## 📧 Contact

If you have questions or suggestions, please create an Issue in the repository.

---

**Version:** 2.0.0

**FastAPI Documentation:** https://lms-core-api-production.up.railway.app/docs

**ReDoc Documentation:** https://lms-core-api-production.up.railway.app/redoc
