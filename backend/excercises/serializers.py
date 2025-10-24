from rest_framework import serializers
from .models import Excercise

class ExcerciseSerializer(serializers.Serializer):
    class Meta:
        model = Excercise
        fields = '__all__'