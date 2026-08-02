from django.db import models
from core.models import TimeStampedModel
class Photo(TimeStampedModel):
    title=models.CharField(max_length=140)
    image=models.ImageField(upload_to='birthday/photos/', blank=True)
    alt_text=models.CharField(max_length=220)
    caption=models.CharField(max_length=240, blank=True)
    is_hero=models.BooleanField(default=False, db_index=True)
    order=models.PositiveIntegerField(default=0, db_index=True)
    class Meta: ordering=('order','title'); indexes=[models.Index(fields=['is_hero','order'])]
    def __str__(self): return self.title
