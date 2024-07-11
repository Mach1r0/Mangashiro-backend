from django.db import models

class Staff(models.Model):
    Role_status = [
        ('Author', 'author'), 
        ('Designer', 'Designer'), 
        ('Director', 'director'), 
        ('Creator', 'Creator'), 
        ('Character Designer', 'Character Designer'), 
    ]
    author = models.CharField(max_length=256)
    role = models.CharField(choices=Role_status, max_length=30, default='Author')