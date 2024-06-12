from django.contrib.auth.models import User
from django.db import models

# Create your models here.

class Seganalazione(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)
    description = models.TextField(verbose_name="Descrizione", blank=True)