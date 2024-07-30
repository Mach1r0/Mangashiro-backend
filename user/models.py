from django.db import models
from anime.models import Anime
from django.utils import timezone
from manga.models import Manga
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.models import AbstractUser, BaseUserManager
from django.contrib.auth import get_user_model
from django.contrib.auth.models import AbstractUser, BaseUserManager
from django.db import models

from django.db import models
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import AbstractUser, BaseUserManager

class UserManager(BaseUserManager):
    use_in_migrations = True

    def create_user(self, email, nickname, password=None, **extra_fields):
        if not email:
            raise ValueError(_('The Email field must be set'))
        if not nickname:
            raise ValueError(_('The Nickname field must be set'))

        email = self.normalize_email(email)
        user = self.model(email=email, nickname=nickname, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, nickname, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        return self.create_user(email, nickname, password, **extra_fields)

class User(AbstractUser):
    username = None
    email = models.EmailField(_('email address'), unique=True)
    nickname = models.CharField(unique=True, max_length=256)
    name = models.CharField(max_length=100)
    background = models.ImageField(upload_to='background-user-img', blank=True, null=True)
    image_profile = models.ImageField(upload_to='profile-img/', blank=True, null=True)
    description = models.CharField(max_length=400, blank=True, null=True)
    description_image = models.ImageField(upload_to='description/', blank=True, null=True)
    anime = models.ManyToManyField('anime.Anime', through='AnimeState', related_name='users')
    manga = models.ManyToManyField('manga.Manga', through='MangaState', related_name='users')

    USERNAME_FIELD = 'nickname'
    REQUIRED_FIELDS = ['email']

    objects = UserManager()

    class Meta:
        verbose_name = _('user')
        verbose_name_plural = _('users')

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
