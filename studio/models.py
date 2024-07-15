from django.db import models
from staff.models import Staff

class Studio(models.Model):
    name = models.CharField(max_length=256)

    def __str__(self) -> str:
        return self.name
