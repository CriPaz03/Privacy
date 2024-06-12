from django.contrib.auth.models import User
from django.db import models

# Create your models here.

class Feedback(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    descrizione = models.TextField(max_length=500, verbose_name="Descrizione", blank=True)

    def __str__(self):
        return f"{self.user.username}: {self.descrizione}"