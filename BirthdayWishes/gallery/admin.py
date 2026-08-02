from django.contrib import admin
from .models import Photo
@admin.register(Photo)
class PhotoAdmin(admin.ModelAdmin):
    list_display=('title','is_hero','order','updated_at'); list_filter=('is_hero',); search_fields=('title','alt_text','caption'); list_editable=('order','is_hero')
