from django.db import models

# Create your models here.
class Staff(models.Model):
    id = models.BigAutoField(primary_key=true)
    autor = models.CharField(max_length=256)
    desenhista  = models.CharField(max_length=256, null=True)
    assistente = models.CharField(max_length=255, null=True)
    