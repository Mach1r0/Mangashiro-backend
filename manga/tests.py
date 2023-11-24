# Import the TestCase class from Django's test module
from django.test import TestCase

# Import the Manga model from the current module
from .models import Manga

# Define a new test case class for the Manga model
class MangaModelTest(TestCase):
    # Class method to set up data for the tests
    @classmethod
    def setUpTestData(cls):
        # Create a new Manga instance that will be used by all test methods
        Manga.objects.create(name='Test Manga', releaseData='2022-01-01', endData='2022-12-31', Description='Test for class manga')
        
    # Test method to check the 'name' attribute of the Manga instance
    def test_name_content(self):
        # Retrieve the Manga instance
        manga = Manga.objects.get(id=1)
        # Define the expected object name
        expected_object_name = f'{manga.name}'
        # Assert that the actual name equals the expected name
        self.assertEquals(expected_object_name, 'Test Manga')

    # Test method to check the 'Description' attribute of the Manga instance
    def test_description_content(self):
        # Retrieve the Manga instance
        manga = Manga.objects.get(id=1)
        # Define the expected object description
        expected_object_description = f'{manga.Description}'
        # Assert that the actual description equals the expected description
        self.assertEquals(expected_object_description, 'Test Description')