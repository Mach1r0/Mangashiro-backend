from django.db import models
from manga.models import Manga
from anime.models import Anime
from django.contrib.auth.models import AbstractUser, BaseUserManager
from django.utils.translation import gettext_lazy as _
from django.utils import timezone
from django.contrib.auth import get_user_model
import json

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
    MANGA_STATE_COMPLETED = 'completed'
    MANGA_STATE_READING = 'reading'
    MANGA_STATE_DROPPED = 'dropped'
    MANGA_STATE_PLANNING = 'planning'

    MANGA_STATE_CHOICES = [
        (MANGA_STATE_COMPLETED, 'Completed'),
        (MANGA_STATE_READING, 'Reading'),
        (MANGA_STATE_DROPPED, 'Dropped'),
        (MANGA_STATE_PLANNING, 'Planning'),
    ]

    ANIME_STATE_COMPLETED = 'completed'
    ANIME_STATE_WATCHING = 'watching'
    ANIME_STATE_DROPPED = 'dropped'
    ANIME_STATE_PLANNING = 'planning'

    ANIME_STATE_CHOICES = [
        (ANIME_STATE_COMPLETED, 'Completed'),
        (ANIME_STATE_WATCHING, 'Watching'),
        (ANIME_STATE_DROPPED, 'Dropped'),
        (ANIME_STATE_PLANNING, 'Planning'),
    ]
    
    username = None
    email = models.EmailField(_('email address'), unique=True)
    nickname = models.CharField(unique=True, max_length=256)
    name = models.CharField(max_length=100)
    background = models.ImageField(upload_to='background-user-img', blank=True, null=True)
    image_profile = models.ImageField(upload_to='profile-img/', blank=True, null=True)
    description = models.CharField(max_length=400, blank=True, null=True)
    description_image = models.ImageField(upload_to='description/', blank=True, null=True)
    manga_states = models.JSONField(default=list, blank=True)
    anime_states = models.JSONField(default=list, blank=True)

    USERNAME_FIELD = 'nickname'
    REQUIRED_FIELDS = ['']

    objects = UserManager()

    class Meta:
        verbose_name = _('user')
        verbose_name_plural = _('users')

    def __str__(self):
        return self.name

    def add_manga_state(self, manga_id, chapters, volume, state, times_read=1):
        if state not in dict(self.MANGA_STATE_CHOICES):
            raise ValueError(f"Estado inválido para manga: {state}")

        state_entry = {
            'manga_id': manga_id,
            'state': state,
            'chapters': chapters, 
            'volume': volume, 
            'times_read': times_read
        }

        self.manga_states = [entry for entry in self.manga_states if entry['manga_id'] != manga_id]
        self.manga_states.append(state_entry)
        self.save()

    def add_anime_state(self, anime_id, state, progress=0, times_watched=1):
        if state not in dict(self.ANIME_STATE_CHOICES):
            raise ValueError(f"Estado inválido para anime: {state}")

        state_entry = {
            'anime_id': anime_id,
            'state': state,
            'progress': progress,
            'times_watched': times_watched
        }
        self.anime_states = [entry for entry in self.anime_states if entry['anime_id'] != anime_id]
        self.anime_states.append(state_entry)
        self.save()

class ReviewManga(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    manga = models.ForeignKey(Manga, on_delete=models.CASCADE, related_name='reviews')
    rating = models.IntegerField(default=0)
    title = models.CharField(max_length=100)
    content = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f'Review by {self.user.name} on {self.date_posted.strftime("%Y-%m-%d")}'

class ReviewAnime(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    anime = models.ForeignKey(Anime, on_delete=models.CASCADE, null=True, blank=True)
    rating = models.IntegerField(default=0)
    title = models.CharField(max_length=100)
    content = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f'Review by {self.user.name} on {self.date_posted.strftime("%Y-%m-%d")}'
