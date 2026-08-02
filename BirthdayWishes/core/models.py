from django.db import models

class TimeStampedModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True, db_index=True)
    updated_at = models.DateTimeField(auto_now=True)
    class Meta:
        abstract = True

class SiteSetting(TimeStampedModel):
    key = models.SlugField(unique=True)
    value = models.TextField(blank=True)
    is_public = models.BooleanField(default=True, db_index=True)
    class Meta:
        ordering = ('key',)
        verbose_name = 'site setting'
        verbose_name_plural = 'site settings'
    def __str__(self): return self.key

class ThemeSetting(TimeStampedModel):
    name = models.CharField(max_length=80, unique=True)
    primary_color = models.CharField(max_length=32, default='#e879f9')
    accent_color = models.CharField(max_length=32, default='#67e8f9')
    glow_color = models.CharField(max_length=32, default='#f0abfc')
    is_active = models.BooleanField(default=True, db_index=True)
    class Meta:
        ordering = ('-is_active','name')
    def __str__(self): return self.name
