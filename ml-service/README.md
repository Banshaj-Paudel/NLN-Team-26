# BurnMap ML Service

This is the predictive model service for BurnMap that forecasts burnout risk.

## For the Frontend Team 🔌

You can interact with `predict-risk` using the following HTTP API.

### Starting the Service
1. Install dependencies: `pip install -r requirements.txt`
2. Run the server: `uvicorn main:app --host 0.0.0.0 --port 8000`
(*Alternatively, use Docker: `docker build -t burnmap-ml .` and `docker run -p 8000:8000 burnmap-ml`*)

### API Endpoint

**URL:** `POST http://localhost:8000/predict-risk`
**Content-Type:** `application/json`

**Request Body Example:**
```json
{
  "sleep_hours": 5.5,
  "mood_score": 2,
  "tasks_completion_rate": 0.8,
  "days_in_stress": 0
}
```

**Fields:**
- `sleep_hours` (float): Hours of sleep (e.g., 5.5, 8.0)
- `mood_score` (int): User's mood score 1–5 (1=bad, 5=great)
- `tasks_completion_rate` (float): % of scheduled tasks completed (0.0 to 1.0)
- `days_in_stress` (int): Consecutive days a user has felt stressed

---

**Response Example:**
```json
{
  "risk_level": "amber",
  "score": 52,
  "reason": "Burnout risk building up. You're in the early warning window — act now before it worsens."
}
```

**Fields:**
- `risk_level` (string): Either `"green"`, `"amber"`, or `"red"`
- `score` (int): A quantitative burnout risk score (higher is worse)
- `reason` (string): A short, human-readable reason detailing the burnout risk

### Note Complete Interactive Docs
Once running, you can visit `http://localhost:8000/docs` to see the interactive Swagger UI and test it directly in the browser!
