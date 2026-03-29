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
    user_id = request.data.get('user_id')
    try:
        user = User.objects.get(id=user_id)
    except User.DoesNotExist:
        return Response({"error": "User not found"}, status=status.HTTP_404_NOT_FOUND)
    
    serializer = CheckInSerializer(data=request.data)
    if serializer.is_valid():
        checkin = serializer.save(user=user)
        # Mock ML endpoint effect
        user.risk_level = "Amber"
        user.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
@permission_classes([AllowAny])
def user_risk_history(request, user_id):
    try:
        user = User.objects.get(id=user_id)
    except User.DoesNotExist:
        return Response({"error": "User not found"}, status=status.HTTP_404_NOT_FOUND)
    
    # Mocking last 7 days risk history
    today = datetime.date.today()
    history = [
        {"date": str(today - datetime.timedelta(days=i)), "risk_score": "Amber"}
        for i in range(7)
    ]
    return Response({"user_id": user_id, "history": history})

@api_view(['GET'])
@permission_classes([AllowAny])
def get_anchors(request):
    anchors = Anchor.objects.all()
    serializer = AnchorSerializer(anchors, many=True)
    return Response(serializer.data)

@api_view(['POST'])
@permission_classes([AllowAny])
def book_session(request):
    user_id = request.data.get('user_id')
    anchor_id = request.data.get('anchor_id')
    
    try:
        user = User.objects.get(id=user_id)
        anchor = Anchor.objects.get(id=anchor_id)
    except (User.DoesNotExist, Anchor.DoesNotExist):
        return Response({"error": "User or Anchor not found"}, status=status.HTTP_404_NOT_FOUND)
        
    data = request.data.copy()
    serializer = SessionSerializer(data=data)
    if serializer.is_valid():
        serializer.save(user=user, anchor=anchor)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
