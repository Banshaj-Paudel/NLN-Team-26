import datetime
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth import get_user_model
from .models import Anchor, CheckIn, Session
from .serializers import AnchorSerializer, CheckInSerializer, SessionSerializer

User = get_user_model()

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
        
        serializer = CheckInSerializer(data=request.data)
        if serializer.is_valid():
            checkin = serializer.save(user=user)
            # Mock ML endpoint effect
            user.risk_level = "Amber"
            user.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
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
        
        # Mocking last 7 days risk history
        today = datetime.date.today()
        history = [
            {"date": str(today - datetime.timedelta(days=i)), "risk_score": "Amber"}
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

@api_view(['POST'])
@permission_classes([AllowAny])
def book_session(request):
    try:
        user_id = request.data.get('user_id')
        anchor_id = request.data.get('anchor_id')
        
        if not user_id or not anchor_id:
            return Response({"error": "Missing required fields: user_id and anchor_id"}, status=status.HTTP_400_BAD_REQUEST)
        
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
