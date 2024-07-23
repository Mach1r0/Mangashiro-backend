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
    image = models.ImageField(upload_to='static/staff-image', blank=True, null=True)
    role = models.CharField(choices=Role_status, max_length=30, default='Author')