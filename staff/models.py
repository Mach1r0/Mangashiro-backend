from django.db import models

class Staff(models.Model):
    autor = models.CharField(max_length=256)
    desenhista  = models.CharField(max_length=256, null=True)
    assistente = models.CharField(max_length=255, null=True)
    