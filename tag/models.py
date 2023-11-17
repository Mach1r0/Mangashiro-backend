from django.db import models

# Create your models here.
class Tag(models.Model):
    id = models.BigAutoField(primary_key=true)
    name = models.CharField(max_length=256)
    description = models.CharField(max_length=256)