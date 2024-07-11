from django.db import models
from staff.models import Staff

class Studio(models.Model):
    name = models.CharField(max_length=256)