from django.db import models

# Create your models here.

class Pkb(models.Model):
    patterns = models.TextField(max_length=500, verbose_name="Patterns", blank=True, null=True)
    strategies = models.TextField(max_length=100, verbose_name="Strategia", blank=True, null=True)
    description = models.TextField(max_length=100, verbose_name="Descrizione", blank=True, null=True)
    context = models.TextField(max_length=100, verbose_name="Contesto", blank=True, null=True)
    mvc = models.TextField(max_length=100, verbose_name="Collocazione MVC", blank=True, null=True)




class Iso(models.Model):
    pkb = models.ForeignKey(Pkb, on_delete=models.CASCADE)
    iso = models.TextField(max_length=100, verbose_name="Iso", blank=True, null=True)