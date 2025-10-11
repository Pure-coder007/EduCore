# 🎓 EduCore API

## 🧭 Overview

**EduCore** is a robust, scalable **School Management System API** built with **Django REST Framework**, **Celery**, and **Redis**.  
It manages students, lecturers, courses, results, and payments — with real-time notifications, wallet transactions, and background email tasks.  

> Built to test and showcase full-stack backend engineering skills, from authentication to async tasks, caching, and Docker orchestration.

---

## 🛠️ Tech Stack

| Component | Description |
|------------|-------------|
| **Backend** | Django 5 + Django REST Framework |
| **Database** | PostgreSQL |
| **Cache & Queue** | Redis + Celery |
| **Auth** | JWT (SimpleJWT) |
| **Containerization** | Docker & Docker Compose |
| **Documentation** | Swagger / drf-yasg |
| **Email Service** | Celery background jobs (SMTP / Mailgun / SendGrid) |

---

## 📦 Features

✅ Student registration with auto-generated matric number  
✅ Wallet system with ₦500 demo credit  
✅ Course registration and result upload  
✅ Lecturer and Admin role management  
✅ Payment tracking and receipts  
✅ Async welcome & notification emails via Celery  
✅ Redis caching for leaderboard and announcements  
✅ API-first design (usable by web or mobile frontend)  

---

## ⚙️ Installation & Setup

### 1️⃣ Clone the Repository
```bash
git clone https://github.com/yourusername/educore.git
cd educore
```

### 2️⃣ Create a `.env` file
```env
SECRET_KEY=your-secret-key
DEBUG=True
DATABASE_URL=postgres://postgres:password@db:5432/educore
REDIS_URL=redis://redis:6379/0
EMAIL_HOST=smtp.gmail.com
EMAIL_HOST_USER=youremail@gmail.com
EMAIL_HOST_PASSWORD=yourpassword
EMAIL_PORT=587
EMAIL_USE_TLS=True
```

### 3️⃣ Run with Docker
```bash
docker-compose up --build
```

Services:
- `web` → Django app  
- `db` → PostgreSQL  
- `redis` → Redis cache  
- `worker` → Celery worker  
- `beat` → Celery beat scheduler  

To view logs:
```bash
docker-compose logs -f web
```

---

## 🧱 Database Models

(See conversation above for model descriptions and endpoints.)

---

## 🚀 API Endpoints

Auth, Student, Lecturer, and Admin endpoints as documented above.

---

## ⚡ Celery Tasks

| Task | Trigger | Description |
|------|----------|-------------|
| `send_welcome_email` | After registration | Send welcome mail |
| `notify_result_release` | Lecturer uploads result | Alert students |
| `notify_payment_approval` | Admin approves payment | Notify student |
| `cache_leaderboard` | Daily (Celery Beat) | Cache top students |

---

## 🧪 Testing

```bash
python manage.py test
```

For Docker:
```bash
docker-compose exec web pytest
```

---

## 🧭 API Docs

Swagger UI → [http://localhost:8000/swagger/](http://localhost:8000/swagger/)  
ReDoc → [http://localhost:8000/redoc/](http://localhost:8000/redoc/)

---

## 🚧 Future Improvements

- Add WebSocket notifications with Django Channels  
- Generate PDF receipts and result slips  
- Implement role-based access middleware  
- Add mobile push notifications  
- Deploy with CI/CD pipeline  

---

## 💡 Developer Notes

- Students get ₦500 demo credit on registration (via signal).  
- Emails are sent via Celery workers (non-blocking).  
- Redis is used for caching frequently accessed data (departments, leaderboard).  
- All sensitive operations (results, payments) require admin approval.

---


/api/v1/
│
├── auth/
│   ├── POST   register/           → Register user
│   ├── POST   login/              → Login user
│   ├── POST   logout/             → Logout user
│   ├── POST   password-reset/     → Request password reset
│   ├── POST   password-reset/confirm/ → Confirm new password
│   ├── GET    profile/            → Get user profile
│   └── PATCH  profile/            → Update profile
│
├── courses/
│   ├── GET    /                   → List all courses
│   ├── POST   /                   → Create course (admin/teacher)
│   ├── GET    /{course_id}/       → Get course details
│   ├── PATCH  /{course_id}/       → Update course
│   ├── DELETE /{course_id}/       → Delete course
│   │
│   └── lessons/
│       ├── GET    /{course_id}/lessons/        → List lessons
│       ├── POST   /{course_id}/lessons/        → Add lesson
│       ├── GET    /{course_id}/lessons/{id}/   → Get lesson
│       ├── PATCH  /{course_id}/lessons/{id}/   → Update lesson
│       └── DELETE /{course_id}/lessons/{id}/   → Delete lesson
│
├── enrollments/
│   ├── POST   /                        → Enroll in course
│   ├── GET    /                        → List user enrollments
│   ├── GET    /{course_id}/students/   → List students in course
│   └── DELETE /{enrollment_id}/        → Unenroll
│
├── payments/
│   ├── POST   initiate/               → Start payment
│   ├── POST   verify/                 → Verify payment
│   ├── GET    /                        → List payments
│   └── GET    /{id}/                   → Payment detail
│
├── assignments/
│   ├── GET    /{course_id}/assignments/           → List assignments
│   ├── POST   /{course_id}/assignments/           → Add assignment
│   ├── GET    /{assignment_id}/                  → Assignment detail
│   ├── POST   /{assignment_id}/submit/           → Submit assignment
│   └── GET    /{assignment_id}/submissions/      → List submissions
│
├── notifications/
│   ├── GET    /                   → List user notifications
│   ├── POST   /                   → Send notification
│   └── PATCH  /{notification_id}/read/ → Mark as read
│
├── admin/
│   ├── GET    users/               → List users
│   ├── PATCH  users/{id}/          → Update user
│   ├── DELETE users/{id}/          → Delete user
│   └── GET    reports/             → Generate reports
│
└── static & media/
    ├── GET /media/{path}
    └── GET /static/{path}


## 🧑‍💻 Author

**Kingsley [Your Surname]**  
Backend Developer • Builder • Football Lover ⚽  
📧 [your.email@example.com]  
🐙 [github.com/yourusername](https://github.com/yourusername)
