from django.test import TestCase
from django.urls import reverse
from .models import HomeExperience

class HomeViewTests(TestCase):
    def test_home_renders_active_experience(self):
        HomeExperience.objects.create(hero_title='Happy Birthday Vishuu', is_active=True)
        response = self.client.get(reverse('birthday:home'))
        self.assertContains(response, 'Happy Birthday Vishuu')
        self.assertContains(response, 'Upload Vishuu')
