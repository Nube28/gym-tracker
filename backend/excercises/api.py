from .models import Excercise
from rest_framework import viewsets, permissions
from .serializers import ExcerciseSerializer

class ExcerciseViewSets(viewsets.ModelViewSet):
    queryset = Excercise.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = ExcerciseSerializer