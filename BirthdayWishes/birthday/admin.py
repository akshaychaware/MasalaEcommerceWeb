from django.contrib import admin
from .models import HomeExperience
@admin.register(HomeExperience)
class HomeExperienceAdmin(admin.ModelAdmin):
    list_display=('hero_title','recipient_name','birthday_label','is_active','updated_at'); list_filter=('is_active',); search_fields=('hero_title','recipient_name')
