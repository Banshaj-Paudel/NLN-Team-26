# Features Implemented So Far

## Backend Setup
- Installed backend dependencies from `backend/requirements.txt`.
- Scaffolded a Django + DRF backend structure under `backend/` with project config and app modules.
- Configured environment-driven settings and PostgreSQL connection via `.env`.

## Apps and Data Models
- Added app modules for `users`, `checkins`, `anchors`, and `sessions`.
- Created models for:
  - Anchor profiles (`anchors`)
  - Daily check-ins with risk score (`checkins`)
  - User-anchor booked sessions (`sessions`)
- Kept users on Django's built-in auth user model.

## API Routes Built
- `POST /checkin`
- `GET /user/:id/risk-history`
- `GET /anchors`
- `POST /session/book`

## Route Behavior
- `POST /checkin` now calls `run_auto_check()` from `burnmap_api/predictor/logic.py` and returns the result directly (no frontend inputs required).
- `GET /user/:id/risk-history` returns recent risk history for the user.
- `GET /anchors` returns available anchors.
- `POST /session/book` books a session between a user and an anchor.

## ML Integration (Current State)
- Added `backend/burnmap_api/predictor/logic.py` with `run_auto_check()`.
- The function currently sends a default payload to ML endpoint (`ML_SERVICE_URL`) and returns ML output.
- Includes a fallback response if ML service is unavailable.

## Seeding and Migrations
- Added demo seed command: `python manage.py seed_demo_data`.
- Seed creates mock users and 10-15 style anchor profiles (currently 12 anchors).
- Ran migrations and verified backend system checks.

## Important Technical Note
- Used unique Django app labels (`users_api`, `checkins_api`, `anchors_api`, `peer_sessions`) to avoid migration/app-label collisions with existing session/postgres state.
