# 🔥 BurnMap — Burnout Early Warning System

## Team
| Dev | Role | Folder |
|-----|------|--------|
| Dev 1 (Lead) | ML Service | `/ml-service` |
| Dev 2 | Backend | `/backend` |
| Dev 3 | Frontend | `/frontend` |
| Dev 4 | Matching | `/matching` |
| Dev 5 | UI/UX + Pitch | — |

## Quick Start

### ML Service (Dev 1)
```bash
cd ml-service
pip install -r requirements.txt
uvicorn main:app --reload --port 8000
# Test: POST http://localhost:8000/predict-risk
```

### Backend (Dev 2)
```bash
cd backend
npm install
cp .env.example .env   # fill in Supabase keys
npm run dev
```

### Frontend (Dev 3)
```bash
cd frontend
npx create-next-app@latest . --typescript --tailwind
npm run dev
```
