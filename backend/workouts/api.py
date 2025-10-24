from .models import ExcerciseDone
from rest_framework import viewsets, permissions
from .serializers import ExcerciseDoneSerializer

class ExcerciseDoneViewSet(viewsets.ModelViewSet):
    queryset = ExcerciseDone.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = ExcerciseDoneSerializer