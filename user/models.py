from django.db import models

class User(models.Model):
    username = models.CharField(max_length=256, null=True,)
    Slug = models.CharField(unique=True,blank=False, null=False,  max_length=50)
    password = models.CharField(max_length=256)
    email = models.CharField(max_length=256)

