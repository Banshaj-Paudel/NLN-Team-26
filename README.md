# 🔥 BurnMap — Burnout Early Warning System

BurnMap is a career stress and burnout prediction system that uses daily behavioural signals (sleep, mood, task completion) to forecast burnout risk and connect users with peer mentors called **Anchors**.

---

## 👥 Team
| Dev | Role | Folder |
|-----|------|--------|
| Dev 1 | ML Service | `/ml-service` |
| Dev 2 | Backend | `/backend` |
| Dev 3 | Frontend | `/frontend` |
| Dev 4 | Matching | `/matching` |
| Dev 5 | UI/UX + Pitch | — |

---

## 🏗️ Architecture

```
Frontend (React + Vite)  →  Backend (Django REST)  →  ML Model (XGBoost)
     localhost:5173               localhost:8000            burnmap_api/predictor
```

---

## ⚙️ Prerequisites

- **Python 3.11+** and [`uv`](https://github.com/astral-sh/uv) (Python package manager)
- **Node.js 18+** and `npm`
- **Homebrew** (macOS) — for `libomp` required by XGBoost
- A `.env` file in `/backend` with your Neon PostgreSQL `DATABASE_URL`

---

## 🚀 Running the Project

### 1. Install System Dependency (first time only)
XGBoost requires the OpenMP library:
```bash
brew install libomp
```

---

### 2. Backend (Django API)

```bash
cd backend

# Install Python dependencies
uv sync

# Set up environment variables
# Create a .env file with:
# DATABASE_URL=postgresql://...your-neon-url...

# Apply database migrations
uv run python manage.py migrate

# Seed mock anchor data (first time only)
uv run python manage.py seed

# Start the server
uv run python manage.py runserver
```
Backend runs at **http://localhost:8000**

---

### 3. Frontend (React + Vite)

Open a **new terminal**:

```bash
cd frontend/frontend-ui

# Install dependencies
npm install

# Create environment file (connects to backend)
echo "VITE_API_BASE_URL=http://localhost:8000" > .env

# Start the dev server
npm run dev
```
Frontend runs at **http://localhost:5173**

---

## 📡 API Endpoints

| Method | Route | Description |
|--------|-------|-------------|
| `POST` | `/onboarding` | Create/update user profile |
| `POST` | `/check-in` | Submit daily check-in, get risk prediction |
| `GET`  | `/user/<id>/risk-history` | Last 7 days of risk scores |
| `GET`  | `/anchors` | List all peer mentors |
| `GET`  | `/anchors/match?user_id=<id>` | Get best matched anchor |
| `GET`  | `/sessions/slots` | Available booking time slots |
| `POST` | `/sessions/book` | Book a session with an anchor |

---

## 🧠 ML Model

The risk prediction model (`backend/burnmap_api/predictor/model.pkl`) is an **XGBoost classifier** trained on `mock_dataset.json`. It takes:

- `sleep_hours` — hours of sleep last night
- `mood_score` — self-reported mood (1–5)
- `tasks_completion_rate` — fraction of planned tasks done (0.0–1.0)
- `days_in_stress` — consecutive days of high stress

And returns a **risk level** (`green` / `amber` / `red`) with a **score** (0–100) and a human-readable **reason**.

---

## 🗃️ Database Schema

| Table | Purpose |
|-------|---------|
| `users_customuser` | User profiles with career stage and stressor tags |
| `api_anchor` | Peer mentor profiles |
| `api_checkin` | Daily behavioural check-ins |
| `api_burnmapresult` | ML prediction results linked to each check-in |
| `api_session` | Booked mentorship sessions |
