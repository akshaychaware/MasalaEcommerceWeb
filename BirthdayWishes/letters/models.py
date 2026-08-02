from django.db import models
from core.models import TimeStampedModel
class BirthdayLetter(TimeStampedModel):
    title=models.CharField(max_length=160, default='A letter for Vishuu')
    body=models.TextField(help_text='Shown with typewriter animation. Replace this placeholder in admin.')
    signature=models.CharField(max_length=120, blank=True)
    is_active=models.BooleanField(default=True, db_index=True)
    class Meta: ordering=('-is_active','-updated_at',)
    def __str__(self): return self.title
