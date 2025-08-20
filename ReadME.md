# Video Sharing Platform (Django + DRF)

A RESTful backend API for a video sharing platform built with **Django**, **Django REST Framework**, and **JWT authentication**. Users can upload videos, comment, favorite, and manage their profiles.

---

## Features

- User Registration & JWT Login (Creator or Consumer)
- Upload video files (local storage)
- View video details and list
- Comment on videos
- Mark videos as Favorite / Unfavorite
- Shared/Unshared comments
- Admin panel with inline display for comments and favorites

---

## Tech Stack

- **Backend**: Django, Django REST Framework
- **Auth**: JWT (via SimpleJWT)
- **Database**: SQLite (default, can switch to PostgreSQL/MySQL)
- **Media Handling**: Local file storage (`/media/videos`)
- **Frontend**: Use with React/Vue or Postman for testing

---

## Setup Instructions

### 1. Clone the Repository

```bash
git clone https://github.com/obaidullah72/video-platform-backend.git
cd video-platform-backend
````

### 2. Create Virtual Environment

```bash
python -m venv env
source env/bin/activate  # or `env\Scripts\activate` on Windows
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Apply Migrations

```bash
python manage.py migrate
```

### 5. Create Superuser

```bash
python manage.py createsuperuser
```

### 6. Run Development Server

```bash
python manage.py runserver
```

---

## Authentication

### Register

POST `/api/register/`
Body:

```json
{
  "username": "john",
  "email": "john@example.com",
  "password": "12345678",
  "is_creator": true
}
```

### Login

POST `/api/login/`
Response:

```json
{
  "access": "JWT_TOKEN",
  "refresh": "REFRESH_TOKEN",
  "user": { "id": 1, "username": "john" }
}
```

Use `access` token in headers:

```http
Authorization: Bearer YOUR_ACCESS_TOKEN
```

---

## API Endpoints

| Method | Endpoint               | Description                |
| ------ | ---------------------- | -------------------------- |
| POST   | `/api/login/`          | User login (JWT)           |
| POST   | `/api/register/`       | User registration          |
| GET    | `/api/profile/`        | Authenticated user profile |
| PATCH  | `/api/profile/`        | Update profile             |
| GET    | `/api/videos/`         | List all videos            |
| POST   | `/api/videos/`         | Upload new video (creator) |
| GET    | `/api/videos/<id>/`    | Retrieve video details     |
| POST   | `/api/comments/`       | Add a comment              |
| POST   | `/api/favorites/`      | Mark video as favorite     |
| DELETE | `/api/favorites/<id>/` | Unfavorite a video         |

---

## File Upload

* Upload videos using `multipart/form-data` with `video` field.
* Files are saved to: `/media/videos/filename.mp4`
* Make sure `MEDIA_URL` and `MEDIA_ROOT` are configured in `settings.py`.

---

## Admin Panel

Login at `/admin/` using superuser credentials.

* Manage users, videos, comments, and favorites.
* Comments and favorites shown inline under each video.

---

## License

This project is open-sourced under the [MIT License](LICENSE).

---

## Contributions

Contributions, issues, and feature requests are welcome!
Feel free to [open an issue](https://github.com/obaidullah72/video-platform-backend/issues).

---

## 📬 Contact

**Developer**: Obaidullah Mansoor
**Email**: [obaidullah3372@gmail.com](mailto:obaidullah3372@gmail.com)
**GitHub**: [obaidullah72](https://github.com/obaidullah72)
