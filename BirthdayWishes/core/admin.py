from django.contrib import admin
from .models import SiteSetting, ThemeSetting
@admin.register(SiteSetting)
class SiteSettingAdmin(admin.ModelAdmin):
    list_display=('key','is_public','updated_at'); list_filter=('is_public',); search_fields=('key','value')
@admin.register(ThemeSetting)
class ThemeSettingAdmin(admin.ModelAdmin):
    list_display=('name','primary_color','accent_color','is_active'); list_filter=('is_active',)
