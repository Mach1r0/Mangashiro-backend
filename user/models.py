from django.db import models
from anime.models import Anime
from django.utils import timezone
from manga.models import Manga

class User(models.Model):
    name = models.CharField(unique=True,blank=False, null=False,  max_length=100)
    nickname = models.CharField(max_length=256, null=True,)
    password = models.CharField(max_length=256)
    background = models.ImageField(upload_to='static/background-user-img', blank=True, null=True)
    image = models.ImageField(upload_to='static/user-img', blank=True, null=True)
    email = models.CharField(max_length=256)
    anime = models.ManyToManyField(Anime, through='AnimeState', related_name='users')
    manga = models.ManyToManyField(Manga, through='MangaState', related_name='users')
    description = models.CharField(max_length=400)
    description_image = models.ImageField(upload_to='description/', blank=True, null=True)
    
    def __str__(self):
        return self.name

class MangaState(models.Model):
    STATE_CHOICES = [
        ('PLANNING', 'Planning to Read'),
        ('COMPLETED', 'Completed'),
        ('READ', 'Read'),
        ('DROPPED', 'Dropped'),
        ('READING', 'Reading'),
    ]

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    manga = models.ForeignKey(Manga, on_delete=models.CASCADE)
    state = models.CharField(max_length=10, choices=STATE_CHOICES)
    times_read = models.PositiveIntegerField(default=1)  # Tracks how many times a manga has been read

    def __str__(self):
        return f"{self.user.name} - {self.manga.title} - {self.state}"

class AnimeState(models.Model):
    STATE_CHOICES = [
        ('PLANNING', 'Planning to Watch'),
        ('COMPLETED', 'Completed'),
        ('WATCHED', 'Watched'),
        ('DROPPED', 'Dropped'),
        ('WATCHING', 'Watching'),
    ]

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    anime = models.ForeignKey(Anime, on_delete=models.CASCADE)
    state = models.CharField(max_length=10, choices=STATE_CHOICES)
    Progress = models.IntegerField()
    times_watched = models.PositiveIntegerField(default=1) 

    def __str__(self):
        return f"{self.user.name} - {self.anime.title} - {self.state}"

class ReviewManga(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    manga = models.ForeignKey(Manga, on_delete=models.CASCADE, null=True, blank=True)
    rating = models.IntegerField(default=0)
    Title = models.CharField(max_length=100)
    content = models.TextField() 
    date_posted = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f'Review by {self.user.name} on {self.date_posted.strftime("%Y-%m-%d")}'

class ReviewAnime(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    anime = models.ForeignKey(Anime, on_delete=models.CASCADE, null=True, blank=True)  
    rating = models.IntegerField(default=0)
    Title = models.CharField(max_length=100)
    content = models.TextField() 
    date_posted = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f'Review by {self.user.name} on {self.date_posted.strftime("%Y-%m-%d")}'
