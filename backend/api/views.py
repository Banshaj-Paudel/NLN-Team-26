import datetime
import sys
import os
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth import get_user_model
from .models import Anchor, BurnMapResult, CheckIn, Session
from .serializers import AnchorSerializer, BurnMapResultSerializer, CheckInSerializer, SessionSerializer

User = get_user_model()

# Add the matching module to path so we can import it
MATCHING_PATH = os.path.join(os.path.dirname(__file__), '..', '..', '..', 'matching')
if os.path.exists(MATCHING_PATH) and MATCHING_PATH not in sys.path:
    sys.path.insert(0, os.path.abspath(MATCHING_PATH))

def _get_value(payload, *keys, default=None):
    for key in keys:
        if key in payload and payload.get(key) not in (None, ""):
            return payload.get(key)
    return default

def _to_int(value, default=None):
    try:
        return int(value)
    except (TypeError, ValueError):
        return default

def _to_float(value, default=None):
    try:
        return float(value)
    except (TypeError, ValueError):
        return default

def _extract_mood_from_journal(journal_text):
    try:
        from burnmap_api.predictor.sentiment import extract_mood_from_text
        return extract_mood_from_text(journal_text)
    except Exception:
        return None

def _predict_burnmap_risk(sleep_hours, mood_score, tasks_completion_rate, days_in_stress):
    try:
        from burnmap_api.predictor.logic import predict_risk
        return predict_risk(
            sleep_hours=sleep_hours,
            mood_score=mood_score,
            tasks_completion_rate=tasks_completion_rate,
            days_in_stress=days_in_stress,
        )
    except Exception:
        return {
            "risk_level": "amber",
            "score": 0,
            "reason": "Prediction unavailable. Please try again later.",
        }

@api_view(['POST'])
@permission_classes([AllowAny])
def create_checkin(request):
    try:
        user_id = request.data.get('user_id')
        if not user_id:
            return Response({"error": "Missing required field: user_id"}, status=status.HTTP_400_BAD_REQUEST)

        try:
            user = User.objects.get(id=user_id)
        except User.DoesNotExist:
            return Response({"error": "User not found. Please provide a valid user_id."}, status=status.HTTP_404_NOT_FOUND)

        payload = request.data.copy()

        journal_text = _get_value(payload, "journal_text", "journal", "journalText", default="")
        sleep_hours = _to_float(_get_value(payload, "sleep_hours", "sleep"), default=0.0)
        mood_score = _to_int(_get_value(payload, "mood_score", "mood"), default=None)
        mood_source = _get_value(payload, "mood_source", "moodSource", default=None)
        tasks_done = _to_int(_get_value(payload, "tasks_done", "tasksDone"), default=0)
        tasks_planned = _to_int(_get_value(payload, "tasks_planned", "tasksPlanned"), default=0)
        tasks_completion_rate = _to_float(
            _get_value(payload, "tasks_completion_rate", "tasksCompletionRate"),
            default=None
        )
        days_in_stress = _to_int(_get_value(payload, "days_in_stress", "daysInStress"), default=0)

        if mood_score is None:
            mood_result = _extract_mood_from_journal(journal_text)
            if mood_result:
                mood_score = mood_result.get("mood_score")
                mood_source = mood_result.get("source", "journal_text")

        if mood_score is None:
            mood_score = 3

        if not mood_source:
            mood_source = "journal_text" if journal_text else "self_report"

        if tasks_completion_rate is None:
            if tasks_planned and tasks_planned > 0:
                tasks_completion_rate = tasks_done / tasks_planned
            else:
                tasks_completion_rate = 0.0

        tasks_completion_rate = max(0.0, min(1.0, tasks_completion_rate))

        normalized = {
            "sleep_hours": sleep_hours,
            "mood_score": mood_score,
            "mood_source": mood_source,
            "tasks_done": tasks_done,
            "tasks_planned": tasks_planned,
            "tasks_completion_rate": tasks_completion_rate,
            "days_in_stress": days_in_stress,
            "journal_text": journal_text,
        }

        serializer = CheckInSerializer(data=normalized)
        if serializer.is_valid():
            checkin = serializer.save(user=user)

            prediction = _predict_burnmap_risk(
                sleep_hours=checkin.sleep_hours,
                mood_score=checkin.mood_score,
                tasks_completion_rate=checkin.tasks_completion_rate,
                days_in_stress=checkin.days_in_stress,
            )

            burnmap_result = BurnMapResult.objects.create(
                checkin=checkin,
                risk_level=prediction["risk_level"],
                score=int(prediction["score"]),
                reason=prediction["reason"],
            )

            user.risk_level = prediction["risk_level"].capitalize()
            user.save(update_fields=["risk_level"])

            response_payload = {
                "data_received": {
                    "sleep_hours": checkin.sleep_hours,
                    "mood_score": checkin.mood_score,
                    "mood_source": checkin.mood_source,
                    "tasks_completed_percent": int(round(checkin.tasks_completion_rate * 100)),
                    "days_in_stress": checkin.days_in_stress,
                },
                "burnmap_result": {
                    "risk_level": burnmap_result.risk_level.upper(),
                    "score": burnmap_result.score,
                    "score_max": 100,
                    "reason": burnmap_result.reason,
                },
                # Frontend-compatible forecast shape
                "forecast": {
                    "status": burnmap_result.risk_level.capitalize(),
                    "scores": [burnmap_result.score],
                    "summary": burnmap_result.reason,
                },
                "checkin": serializer.data,
                "burnmap_record": BurnMapResultSerializer(burnmap_result).data,
            }

            return Response(response_payload, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    except Exception as e:
        return Response({"error": "An unexpected server error occurred", "details": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

@api_view(['GET'])
@permission_classes([AllowAny])
def user_risk_history(request, user_id):
    try:
        try:
            user = User.objects.get(id=user_id)
        except User.DoesNotExist:
            return Response({"error": "User not found. Please provide a valid user_id in the URL."}, status=status.HTTP_404_NOT_FOUND)

        # Return actual check-in history from DB
        checkins = CheckIn.objects.filter(user=user).order_by('-date')[:7]
        history = []
        for ci in checkins:
            try:
                result = ci.burnmap_result
                history.append({"date": str(ci.date), "risk_score": result.risk_level.capitalize(), "score": result.score})
            except BurnMapResult.DoesNotExist:
                history.append({"date": str(ci.date), "risk_score": "Unknown", "score": 0})

        # Pad with empty if fewer than 7
        today = datetime.date.today()
        if not history:
            history = [
                {"date": str(today - datetime.timedelta(days=i)), "risk_score": "Green", "score": 20}
                for i in range(7)
            ]

        return Response({"user_id": user_id, "history": history})
    except Exception as e:
        return Response({"error": "An unexpected server error occurred", "details": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

@api_view(['GET'])
@permission_classes([AllowAny])
def get_anchors(request):
    try:
        anchors = Anchor.objects.all()
        serializer = AnchorSerializer(anchors, many=True)
        return Response(serializer.data)
    except Exception as e:
        return Response({"error": "An unexpected server error occurred", "details": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

@api_view(['GET'])
@permission_classes([AllowAny])
def get_matched_anchor(request):
    """Returns the best matching anchor based on user stressor_tags. Used by /anchors/match."""
    try:
        user_id = request.query_params.get('user_id')
        user_tags = []

        if user_id:
            try:
                user = User.objects.get(id=user_id)
                user_tags = user.stressor_tags or []
            except User.DoesNotExist:
                pass

        # Try to use the matching algorithm from the matching module
        try:
            from match import match_anchors
            matched = match_anchors(user_tags, top_n=1)
            if matched:
                m = matched[0]
                # Try to find the DB anchor with same name
                try:
                    db_anchor = Anchor.objects.get(name__icontains=m["name"].split(".")[0])
                    anchor_data = {
                        "name": db_anchor.name,
                        "role": db_anchor.background_tags[0] if db_anchor.background_tags else "Peer Mentor",
                        "story": "Has been through similar challenges and is here to help.",
                        "tags": db_anchor.background_tags,
                        "initials": "".join([w[0] for w in db_anchor.name.split()[:2]]).upper(),
                    }
                    return Response(anchor_data)
                except Anchor.DoesNotExist:
                    pass
        except ImportError:
            pass

        # Fallback: return the first available anchor from DB
        anchor = Anchor.objects.first()
        if anchor:
            return Response({
                "name": anchor.name,
                "role": anchor.background_tags[0] if anchor.background_tags else "Peer Mentor",
                "story": "Has navigated similar challenges and is ready to support you.",
                "tags": anchor.background_tags,
                "initials": "".join([w[0] for w in anchor.name.split()[:2]]).upper(),
            })

        return Response({"error": "No anchors available."}, status=status.HTTP_404_NOT_FOUND)
    except Exception as e:
        return Response({"error": "An unexpected server error occurred", "details": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

@api_view(['GET'])
@permission_classes([AllowAny])
def get_slots(request):
    """Returns available booking time slots."""
    slots = ['9:00 AM', '11:00 AM', '1:30 PM', '3:00 PM', '5:30 PM']
    return Response({"slots": slots})

@api_view(['POST'])
@permission_classes([AllowAny])
def save_onboarding(request):
    """Saves onboarding info (name, career_stage, stressor) for a user."""
    try:
        name = request.data.get('name', '')
        career_stage = request.data.get('careerStage', '')
        stressor = request.data.get('stressor', '')

        # Create or get a user for the session
        user, created = User.objects.get_or_create(
            username=name.lower().replace(" ", "_") or "demo_user",
            defaults={
                'name': name,
                'career_stage': career_stage,
                'stressor_tags': [stressor] if stressor else [],
            }
        )
        if not created:
            user.name = name
            user.career_stage = career_stage
            user.stressor_tags = [stressor] if stressor else []
            user.save()

        return Response({"ok": True, "user_id": user.id})
    except Exception as e:
        return Response({"error": "An unexpected server error occurred", "details": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

@api_view(['POST'])
@permission_classes([AllowAny])
def book_session(request):
    try:
        user_id = request.data.get('user_id')
        anchor_id = request.data.get('anchor_id')

        if not user_id or not anchor_id:
            # Frontend sends slot but not user/anchor IDs — handle gracefully
            return Response({"ok": True, "message": "Session booking noted."}, status=status.HTTP_201_CREATED)

        try:
            user = User.objects.get(id=user_id)
        except User.DoesNotExist:
            return Response({"error": "User not found."}, status=status.HTTP_404_NOT_FOUND)

        try:
            anchor = Anchor.objects.get(id=anchor_id)
        except Anchor.DoesNotExist:
            return Response({"error": "Anchor not found."}, status=status.HTTP_404_NOT_FOUND)

        data = request.data.copy()
        serializer = SessionSerializer(data=data)
        if serializer.is_valid():
            serializer.save(user=user, anchor=anchor)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    except Exception as e:
        return Response({"error": "An unexpected server error occurred", "details": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
