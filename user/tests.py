from django.test import TestCase
from .models import User  # It should be .models not .model

class TestUser(TestCase):  # Use TestUser instead of Testeuser and it should inherit from TestCase
    @classmethod
    def setUpTestData(cls):
        User.objects.create(username='Test User', password='12345678', email='daniel@gmail.com')

    def test_username(self):  # Use test_username instead of teste_username
        user = User.objects.get(id=1)  # Use User.objects.get(id=1) instead of user(id=1)
        expected_object_name = 'Test User'  # Use 'Test User' instead of f'{User.name}'
        self.assertEquals(user.username, expected_object_name)  # Use user.username instead of expected_object_name

    def test_password(self):  # Use test_password instead of teste_password
        user = User.objects.get(id=1)
        expected_object_password = '12345678'  # Use '12345678' instead of f'{User.password}'
        self.assertEquals(user.password, expected_object_password)  # Use user.password instead of expected_object_name

    def test_email(self):  # Use test_email instead of teste_gmail
        user = User.objects.get(id=1)
        expected_object_email = 'daniel@gmail.com'  # Use 'daniel@gmail.com' instead of f'{User.gmail}'
        self.assertEquals(user.email, expected_object_email)  # Use user.email instead of expected_object_name