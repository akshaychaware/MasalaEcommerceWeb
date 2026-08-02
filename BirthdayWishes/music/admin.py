from django.contrib import admin
from .models import Track
@admin.register(Track)
class TrackAdmin(admin.ModelAdmin):
    list_display=('title','artist','order','is_active'); list_filter=('is_active',); list_editable=('order','is_active'); search_fields=('title','artist')
