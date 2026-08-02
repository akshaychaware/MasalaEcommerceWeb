from django.contrib import admin
from .models import Reason, SecretMessage
@admin.register(Reason)
class ReasonAdmin(admin.ModelAdmin):
    list_display=('title','icon','order','is_published'); list_filter=('is_published',); list_editable=('order','is_published'); search_fields=('title','front_text','back_text')
@admin.register(SecretMessage)
class SecretMessageAdmin(admin.ModelAdmin):
    list_display=('title','is_active','updated_at'); list_filter=('is_active',); search_fields=('title','message')
