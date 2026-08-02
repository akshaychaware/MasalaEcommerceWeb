from django.contrib import admin
from .models import BirthdayLetter
@admin.register(BirthdayLetter)
class BirthdayLetterAdmin(admin.ModelAdmin):
    list_display=('title','is_active','updated_at'); list_filter=('is_active',); search_fields=('title','body')
