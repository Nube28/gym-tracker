from .models import Day, DayExcercise, Routine
from rest_framework import viewsets, permissions
from .serializers import DaySerializer, DayExcerciseSerializer, RoutineSerializer

class DayViewSet(viewsets.ModelViewSet):
    queryset = Day.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = DaySerializer

class DayExcerciseViewSet(viewsets.ModelViewSet):
    queryset = DayExcercise.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = DayExcerciseSerializer

class RoutineViewSet(viewsets.ModelViewSet):
    queryset = Routine.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = RoutineSerializer