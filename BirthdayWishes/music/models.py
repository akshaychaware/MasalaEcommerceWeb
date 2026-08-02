from django.db import models
from core.models import TimeStampedModel
class Track(TimeStampedModel):
    title=models.CharField(max_length=160)
    artist=models.CharField(max_length=120, blank=True)
    audio=models.FileField(upload_to='birthday/music/', blank=True)
    external_url=models.URLField(blank=True)
    order=models.PositiveIntegerField(default=0, db_index=True)
    is_active=models.BooleanField(default=True, db_index=True)
    class Meta: ordering=('order','title')
    def __str__(self): return self.title
