from rest_framework import serializers
from .models import ExcerciseDone

class ExcerciseDoneSerializer(serializers.Serializer):
    class Meta:
        model = ExcerciseDone
        fields = '__all__'