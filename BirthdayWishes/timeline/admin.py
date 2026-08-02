from django.contrib import admin
from .models import TimelineEvent
@admin.register(TimelineEvent)
class TimelineEventAdmin(admin.ModelAdmin):
    list_display=('title','event_date','order','is_published'); list_filter=('is_published',); search_fields=('title','description'); list_editable=('order','is_published')
