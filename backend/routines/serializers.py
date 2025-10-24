from rest_framework import serializers
from .models import Day, DayExcercise, Routine

class DaySerializer(serializers.ModelSerializer):
    class Meta:
        model = Day
        fields = '__all__'

class DayExcerciseSerializer(serializers.ModelField):
    class Meta:
        model = DayExcercise
        fields = '__all__'

class RoutineSerializer(serializers.ModelField):
    class Meta:
        model = Routine
        fileds = '__all__'