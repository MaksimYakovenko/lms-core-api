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

<project structure details here>

## 📑 Kafka Topics

Detailed information about the system's relevant Kafka topics includes the following:

###  Legal Entity (Business Entity)
- **Topic Name**: Legal Entity
- **Entity Name**: Legal Entity
- **Data Catalog**: [Link](https://datacatalog.epam.com/data/data-details/255703/summary?utm_source=onehub-assistant&utm_medium=widget)
- **Steward**: Not specified

###  legalentity (Data Entity)
- **Topic Name**: legalentity
- **Entity Name**: legalentity
- **Data Catalog**: [Link](https://datacatalog.epam.com/data/data-details/89573/summary?utm_source=onehub-assistant&utm_medium=widget)
- **Steward**: Not specified

###  legal_entity (Data Entity)
- **Topic Name**: legal_entity
- **Entity Name**: legal_entity
- **Data Catalog**: [Link](https://datacatalog.epam.com/data/data-details/129899/summary?utm_source=onehub-assistant&utm_medium=widget)
- **Steward**: Not specified
