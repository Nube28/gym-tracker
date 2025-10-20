from django.db import models
from users.models import CustomUser;

# Create your models here.
class Excercise (models.Model):
    EQUIPMENT_CHOICES = [
        ('ninguno', 'Ninguno'),
        ('mancuernas', 'Mancuernas'),
        ('cable', 'Cable'),
        ('barra', 'Barra'),
        ('maquina', 'Máquina'),
        ('banda', 'Banda elástica'),
        ('otro', 'Otro'),
    ]
    
    name = models.CharField(max_length=100)
    muscle_main = models.CharField(max_length=50)
    muscle_secondary = models.CharField(max_length=50, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    equipment =  models.CharField(max_length=50, choices=EQUIPMENT_CHOICES)
    created_by = models.ForeignKey(CustomUser, on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return self.name