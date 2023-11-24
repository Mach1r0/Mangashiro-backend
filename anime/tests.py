from django.test import TestCase
from .models import Anime

class AnimeModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        Anime.objects.create(name='Test Anime', releaseData='2023-11-23', endData='2025-11-23', Description='Test for class anime')
        
    def test_name_content(self):
        anime = Anime.objects.get(id=1)
        expected_object_name = 'Test Anime'
        self.assertEquals(anime.name, expected_object_name)
        
    def test_description_content(self):
        anime = Anime.objects.get(id=1)
        expected_object_description = 'Test for class anime'
        self.assertEquals(anime.Description, expected_object_description)