# 🧠 BurnMap ML Predictor: Integration Instructions

This document is for the frontend/backend teams who need to integrate the ML Service into their respective applications.

## 📝 1. Description of the Model
The `ml-service` uses a custom predictive model to forecast a user's likelihood of experiencing burnout. It analyzes four primary behavioral and situational vectors:
1. **Sleep deficit** (Quantity of sleep)
2. **Mood/Sentiment** (Emotional well-being)
3. **Task Completion** (Productivity and workload management)
4. **Days in Stress** (Prolonged exposure to high-pressure scenarios)

The model evaluates these inputs and calculates a cumulative "Risk Score" out of 100, which is then mapped securely to one of three risk levels (`green`, `amber`, `red`). The service wraps this logic in an interactive HTTP layer using **FastAPI**.

---

## ⚙️ 2. Prerequisites
To run the ML microservice on your local machine, you need **Python (3.9+)**.

1. Navigate to the `ml-service` folder.
2. (Optional but recommended) Create a virtual environment:
   ```bash
   python3 -m venv venv
   source venv/bin/activate
   ```
3. Install the required Python packages:
   ```bash
   pip install -r requirements.txt
   ```

---

## 🚀 3. How to Start the Service
Start the server using Uvicorn. By default, it will listen on `localhost` port `8000`.

```bash
uvicorn main:app --host 0.0.0.0 --port 8000
```
*(You will know it is running successfully when you see `Uvicorn running on http://0.0.0.0:8000` in the terminal output).*

**Using Docker?** If you prefer, you can build and run it via the included Dockerfile:
```bash
docker build -t burnmap-ml .
docker run -p 8000:8000 burnmap-ml
```

---

## 🔌 4. The Interactive API Endpoint
Once the server is running, the frontend and backend can interact with it via a straightforward HTTP POST request.

- **Endpoint:** `POST http://localhost:8000/predict-risk`
- **Headers:** `Content-Type: application/json`
- **CORS:** Enabled globally. You can fetch this directly from `localhost:5173` (Vite) or any other origins.

### What it TAKES (Request Payload)
Send a JSON payload with the following four keys. Every key must be provided.

| Field | Type | Expected Range | Description |
|-------|------|----------------|-------------|
| `sleep_hours` | `float` | `0.0` - `24.0` | Hours of sleep the user reported last night. |
| `mood_score` | `int` | `1` - `5` | Psychological state (1 is severely negative, 5 is completely positive). |
| `tasks_completion_rate` | `float` | `0.0` - `1.0` | Percentage of tasks finished vs. assigned. E.g., `0.85` means 85%. |
| `days_in_stress` | `int` | `0` or higher | Consecutive days the user has been feeling stressed. |

**Example Request body:**
```json
{
  "sleep_hours": 4.5,
  "mood_score": 2,
  "tasks_completion_rate": 0.45,
  "days_in_stress": 3
}
```

### What it GIVES (Response Payload)
The model will output a structured JSON response identifying the stress category alongside the actual calculated score and a human-readable interpretation.

| Field | Type | Description |
|-------|------|-------------|
| `risk_level` | `string` | The burnout severity: `"green"`, `"amber"`, or `"red"`. |
| `score` | `int` | The aggregate risk score evaluated by the model. |
| `reason` | `string` | A human-readable contextual explanation suitable for displaying on a UI card. |

**Example Response body:**
```json
{
  "risk_level": "amber",
  "score": 55,
  "reason": "Burnout risk building up. You're in the early warning window — act now before it worsens."
}
```

---

## 🎮 5. Test Live using Swagger UI
If you want to manually interact with and test the variables before hard-coding them into your frontend app, FastAPI generates an automatic playground.
- While the server is running, visit: **http://localhost:8000/docs** in your browser.
- Click `POST /predict-risk`, hit `Try it out`, alter the JSON fields and execute!
