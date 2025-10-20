from django.db import models
from users.models import CustomUser
from excercises.models import Excercise

# Esta es la rutina en la que se guardaran todo, solo es un "contenedor"
class Routine(models.Model): 
    name = models.CharField(max_length=100)
    description = models.TextField()
    is_public = models.BooleanField(default=False)
    created_at = models.DateField(auto_now_add=True)

    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='routines')

    def __str__(self):
        return f"{self.name} - {self.user.username}"

# Este es el dia planeado, donde se tienen los ejercicios que se van a hacer ese dia 
# Guardados en la rutina u know?
class Day(models.Model):
    name = models.CharField()
    order = models.PositiveIntegerField(default=1)
    
    routine = models.ForeignKey(Routine, on_delete=models.CASCADE, related_name='days')
    excercise = models.ManyToManyField(Excercise, through='DayExcercise')

    def __str__(self):
        return f"{self.name} ({self.routine.name})"
    
# Esto es el ejercicio que se tiene planeado, cuantas sets y reps se supone que 
# planeaste
class DayExcercise(models.Model):
    sets = models.PositiveIntegerField(default=3)
    reps = models.PositiveIntegerField(default=12)

    day = models.ForeignKey(Day, on_delete=models.CASCADE)
    excercise = models.ForeignKey(Excercise, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.excercise.name} - {self.day.name}"