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

## 🛠 Kafka Topics Section

### Kafka Topics Documentation

#### `epm-skls-ai.courses-to-take`

- **Data Entity Name:** `epm-skls-ai.courses-to-take`
- **Data Steward Email:** Not specified
- **Data Catalog Link:** [https://datacatalog.epam.com/data/data-details/622664/summary?utm_source=onehub-assistant&utm_medium=widget](https://datacatalog.epam.com/data/data-details/622664/summary?utm_source=onehub-assistant&utm_medium=widget)

This topic is used for reporting and analytical purposes in the LMS application. The data steward and responsible department should ensure data integrity and publish guidelines for usage.

---

More details on Kafka utilization within the LMS system will be documented here as needed.
