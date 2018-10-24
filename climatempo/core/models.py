from django.db import models

class Consulta(models.Model):
    consulta = models.TextField(max_length=2000)
