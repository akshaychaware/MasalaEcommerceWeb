from django.db import models
from core.models import TimeStampedModel
class Reason(TimeStampedModel):
    title=models.CharField(max_length=120)
    front_text=models.CharField(max_length=180)
    back_text=models.TextField()
    icon=models.CharField(max_length=16, default='✨')
    order=models.PositiveIntegerField(default=0, db_index=True)
    is_published=models.BooleanField(default=True, db_index=True)
    class Meta: ordering=('order','title')
    def __str__(self): return self.title
class SecretMessage(TimeStampedModel):
    title=models.CharField(max_length=140, default='One tiny secret')
    message=models.TextField()
    is_active=models.BooleanField(default=True, db_index=True)
    class Meta: ordering=('-is_active','-updated_at')
    def __str__(self): return self.title
