from django.db import models
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
    REQUIRED_FIELDS = ['email']

    objects = UserManager()

    class Meta:
        verbose_name = _('user')
        verbose_name_plural = _('users')

    def __str__(self):
        return self.name

    def add_manga_state(self, manga_id, state, times_read=1):
        state_entry = {
            'manga_id': manga_id,
            'state': state,
            'times_read': times_read
        }
        self.manga_states = [entry for entry in self.manga_states if entry['manga_id'] != manga_id]
        self.manga_states.append(state_entry)
        self.save()

    def add_anime_state(self, anime_id, state, progress=0, times_watched=1):
        state_entry = {
            'anime_id': anime_id,
            'state': state,
            'progress': progress,
            'times_watched': times_watched
        }
        self.anime_states = [entry for entry in self.anime_states if entry['anime_id'] != anime_id]
        self.anime_states.append(state_entry)
        self.save()

class Manga(models.Model):
    # Defina os campos do modelo Manga conforme necessário
    title = models.CharField(max_length=255)

    def __str__(self):
        return self.title

class Anime(models.Model):
    # Defina os campos do modelo Anime conforme necessário
    title = models.CharField(max_length=255)

    def __str__(self):
        return self.title

class ReviewManga(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    manga = models.ForeignKey(Manga, on_delete=models.CASCADE, null=True, blank=True)
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
