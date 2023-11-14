from django.db import models

# Create your models here.
class User(models.Model):
    id = models.BigAutoField(primary_key=True)
    username = models.CharField(max_length=256)
    password = models.CharField(max_length=256)
    email = models.CharField(max_length=256)

