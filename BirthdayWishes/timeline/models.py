from django.db import models
from core.models import TimeStampedModel
class TimelineEvent(TimeStampedModel):
    eyebrow=models.CharField(max_length=80, blank=True)
    title=models.CharField(max_length=160)
    description=models.TextField()
    event_date=models.CharField(max_length=80, blank=True)
    order=models.PositiveIntegerField(default=0, db_index=True)
    is_published=models.BooleanField(default=True, db_index=True)
    class Meta: ordering=('order','title'); indexes=[models.Index(fields=['is_published','order'])]
    def __str__(self): return self.title
