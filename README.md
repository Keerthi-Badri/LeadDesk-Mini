# LeadDesk Mini

LeadDesk Mini is a full-stack lead management application that allows users to submit business leads and admins to securely manage and track them.

## Live Demo

Frontend:
https://lead-desk-mini-zzov-4mqxwmezq-keerthis-projects-55e96772.vercel.app/

Backend:
https://leaddesk-mini-production-9913.up.railway.app/

---

## Features

### User Features
- Submit lead details
- Store leads in database
- Receive submission confirmation

### Admin Features
- Secure admin login
- JWT-based authentication
- View all leads
- Search leads by name or email
- Update lead status

---

# Tech Stack

## Frontend
- React.js
- Vite
- Axios
- React Router

## Backend
- Python
- Flask
- Flask JWT Extended
- bcrypt

## Database
- MySQL

## Deployment
- Vercel (Frontend)
- Railway (Backend and Database)

---

# Database Model

## admins Table

| Column | Description |
|---|---|
| id | Primary key |
| email | Admin email |
| password | Hashed password |

Passwords are stored securely using bcrypt hashing.

---

## leads Table

| Column | Description |
|---|---|
| id | Primary key |
| name | Customer name |
| email | Customer email |
| budget | Project budget |
| message | Project description |
| status | Lead status |
| created_at | Lead creation time |

---

# Authentication Approach

Admin authentication is implemented using JWT tokens.

Authentication flow:

1. Admin enters email and password.
2. Backend checks admin details from MySQL database.
3. Password is verified using bcrypt.
4. Backend generates a JWT token.
5. Frontend stores the token.
6. Protected APIs require JWT authentication.

---

# Admin Test Credentials

Email:

admin@leaddesk.com

Password:

admin123

---

# Local Setup

## Backend

```bash
cd backend
pip install -r requirements.txt
python app.py
