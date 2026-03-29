from rest_framework.response import Response
from rest_framework.views import APIView

from burnmap_api.predictor.logic import run_auto_check, run_check_from_input


class CheckInCreateAPIView(APIView):
    def post(self, request):
        payload = request.data if isinstance(request.data, dict) else {}

        if {"sleep", "mood", "tasksDone", "tasksPlanned"}.issubset(payload.keys()):
            sleep_hours = float(payload.get("sleep", 7))
            mood_10 = int(payload.get("mood", 6))
            mood_score = max(1, min(5, round(mood_10 / 2)))
            tasks_done = float(payload.get("tasksDone", 0))
            tasks_planned = float(payload.get("tasksPlanned", 1))
            tasks_completion_rate = 0.0 if tasks_planned <= 0 else max(0.0, min(1.0, tasks_done / tasks_planned))
            days_in_stress = int(payload.get("daysInStress", 2))

            result = run_check_from_input(
                sleep_hours=sleep_hours,
                mood_score=mood_score,
                tasks_completion_rate=tasks_completion_rate,
                days_in_stress=days_in_stress,
            )
        else:
            result = run_auto_check()

        score = int(result.get("score", 0))
        trend = [
            max(0, score - 18),
            max(0, score - 14),
            max(0, score - 10),
            max(0, score - 7),
            max(0, score - 4),
            max(0, score - 2),
            score,
        ]

        response_payload = {
            **result,
            "status": str(result.get("risk_level", "amber")).capitalize(),
            "scores": trend,
            "summary": result.get("reason", "Risk analysis completed."),
        }
        return Response(response_payload)
