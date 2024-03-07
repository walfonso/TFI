from django.db import models

# Create your models here.
from django.db import models
class Candidato(models.Model):
  name = models.CharField(max_length=100, null=True)
  experiencia = models.FloatField()
  idioma = models.FloatField()
  ve = models.FloatField()
  fys = models.FloatField()
  candidato = models.IntegerField(choices=[(1, 'Regular'), (2, 'Bueno'), (3, 'Muy Bueno')])
