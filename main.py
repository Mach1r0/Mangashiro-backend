import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'your_project.settings')
django.setup()


import json
from django.core.management.base import BaseCommand
from user.models import User, AnimeState, ReviewManga, ReviewAnime
from manga.models import Manga 
from studio.models import Studio 
from staff.models import Staff 
from tag.models import Tag
from character.models import Character
from anime.models import Anime 


def populate_database():
    pass

if __name__ == "__main__":
    populate_database()
    print("Database populated successfully!")
