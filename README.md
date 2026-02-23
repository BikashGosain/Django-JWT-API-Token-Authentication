# Django JWT API Token Authentication

A Django REST Framework project implementing JWT (JSON Web Token) authentication with role-based access control, plus a custom frontend UI (no DRF browsable API). Built while learning from a YouTube tutorial.
---
view live: https://django-jwt-api-token-authentication.onrender.com

## Features

<a href="https://web-based-blogging-platform-with-content.onrender.com" target="_blank"><img src="https://img.shields.io/badge/🚀_Live_Demo-46E3B7?style=for-the-badge" /></a>

- User registration with optional role assignment
- JWT-based login (access & refresh tokens)
- Role-based access control via custom permissions
- Protected dashboard endpoint with role display
- Full SimpleJWT token endpoints (obtain, refresh, verify)
- Custom HTML/CSS frontend (register, login, dashboard pages)

## Project Structure

```
djangojwt/
├── djangojwt/               # Project config
│   ├── settings.py
│   ├── urls.py
│   ├── asgi.py
│   └── wsgi.py
├── myapp/                   # Main application
│   ├── migrations/
│   ├── templates/           # Frontend HTML pages
│   │   ├── login.html
│   │   ├── register.html
│   │   └── dashboard.html
│   ├── models.py            # Role & UserRole models
│   ├── serializers.py       # Register, Login, User serializers (includes roles)
│   ├── views.py             # Register, Login, Dashboard views
│   ├── permission.py        # Custom HasRole permission
│   ├── admin.py
│   └── apps.py
├── manage.py
├── db.sqlite3
└── requirements.txt
```

## Tech Stack

- Python 3.x
- Django 5.x
- Django REST Framework
- djangorestframework-simplejwt
- django-cors-headers

## Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/BikashGosain/Django-JWT-API-Token-Authentication.git
   cd Django-JWT-API-Token-Authentication
   ```

2. **Create and activate a virtual environment**
   ```bash
   python -m venv env
   # Windows
   env\Scripts\activate
   # macOS/Linux
   source env/bin/activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Run migrations**
   ```bash
   python manage.py migrate
   ```

5. **Start the development server**
   ```bash
   python manage.py runserver
   ```

6. **Open in browser**
   ```
   http://127.0.0.1:8000/
   ```

## Frontend Pages

| URL | Description |
|-----|-------------|
| `/` | Redirects to login |
| `/login/` | Login page |
| `/register/` | Register page |
| `/dashboard/` | Protected dashboard (requires login) |

## API Endpoints

| Method | Endpoint | Auth Required | Description |
|--------|----------|---------------|-------------|
| POST | `/api/auth/register/` | No | Register a new user |
| POST | `/api/auth/login/` | No | Login and receive JWT tokens |
| GET | `/api/dashboard/` | Yes + Role | Access protected dashboard |
| POST | `/api/token/` | No | Obtain JWT token pair |
| POST | `/api/token/refresh/` | No | Refresh access token |
| POST | `/api/token/verify/` | No | Verify a token |

## Usage Examples

### Register a User
```http
POST /api/auth/register/
Content-Type: application/json

{
  "username": "john",
  "email": "john@example.com",
  "password": "securepassword",
  "role": "Teacher"
}
```

### Login
```http
POST /api/auth/login/
Content-Type: application/json

{
  "username": "john",
  "password": "securepassword"
}
```

**Response:**
```json
{
  "refresh": "<refresh_token>",
  "access": "<access_token>",
  "user": {
    "id": 1,
    "username": "john",
    "email": "john@example.com",
    "roles": ["Teacher"]
  }
}
```

### Access Dashboard (Teacher role required)
```http
GET /api/dashboard/
Authorization: Bearer <access_token>
```

## Role-Based Access Control

Roles are stored in the `Role` model and linked to users via `UserRole`. The custom `HasRole` permission checks whether the authenticated user holds the role required by a given view. For example, `DashboardView` requires the `Teacher` role.

The `UserSerializer` returns all roles assigned to a user via a `SerializerMethodField`, so roles are visible on the dashboard frontend after login.

## Models

**Role** — stores role names (e.g. `Teacher`, `Student`).

**UserRole** — a many-to-many bridge between Django's built-in `User` and `Role`, with a timestamp of when the role was assigned.

---

*This project was built for learning purposes following a YouTube tutorial on Django JWT authentication.*
