from django.db import models
from users.models import CustomUser
from routines.models import Day
from excercises.models import Excercise

# Historial de los ejercicios sabes? 
# representa literalmente el ejercicio hecho salu2
class ExcerciseDone(models.Model):
    date = models.DateField(auto_now_add=True)
    weight_used = models.FloatField(blank=True, null=True)
    reps_done = models.FloatField(blank=True, null=True)
    note = models.TextField(blank=True, null=True)

    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    excercise = models.ForeignKey(Excercise, on_delete=models.CASCADE)
    day = models.ForeignKey(Day, on_delete=models.SET_NULL, null=True, blank=True)
    
    def __str__(self):
        return f"{self.exercise.name} - {self.user.username} ({self.date})"

