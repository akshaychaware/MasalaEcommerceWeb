from django.db import models
from core.models import TimeStampedModel

class HomeExperience(TimeStampedModel):
    recipient_name = models.CharField(max_length=120, default='Vishuukhaa', db_index=True)
    nickname = models.CharField(max_length=80, default='Vishuu')
    birthday_label = models.CharField(max_length=80, default='11 August')
    hero_title = models.CharField(max_length=180, default='Happy Birthday Vishuu')
    hero_subtitle = models.CharField(max_length=260, default='A cinematic little universe made just for you.')
    cta_label = models.CharField(max_length=80, default='Begin the magic')
    ending_message = models.TextField(default='May your year be as luminous, brave, and beautiful as your smile.')
    is_active = models.BooleanField(default=True, db_index=True)
    class Meta:
        ordering = ('-is_active','-updated_at')
        verbose_name = 'home experience'
    def __str__(self): return self.hero_title
