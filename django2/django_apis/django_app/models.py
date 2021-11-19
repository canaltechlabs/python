from django.db import models

# Create your models here.
class Serie(models.Model):

    titulo = models.CharField(max_length=255)
    sinopse = models.TextField(max_length=255, blank=True, null=True)
    quantidade_episodios = models.IntegerField()