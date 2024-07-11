from django.db import models
from datetime import datetime
from django.contrib.auth.models import User

# Create your models here.
class Comentario(models.Model):
    data = models.DateTimeField(default=datetime.now)
    comentario = models.CharField(max_length=300)
    ativo = models.BooleanField(default=True)
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    def __str__(self):
        return self.comentario
    
