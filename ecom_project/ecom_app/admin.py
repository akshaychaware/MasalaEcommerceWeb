from django.contrib import admin
from .models import *
# Register your models here.
# @admin.register(Masala)
# class MasalaAdmin(admin.ModelAdmin):
#     list_display=('name','img','prize','mrp','discount')
    

# @admin.register(cart)
# class cartAdmin(admin.ModelAdmin):
#     list_display=('uid','pid','qty')

@admin.register(order)
class orderAdmin(admin.ModelAdmin):
   list_display=('order_id','uid','pid','qty')

@admin.register(Masala)
class MasalaAdmin(admin.ModelAdmin):
    list_display=('name','quantity','unit','prize','mrp','discount','note','ingredients','recipe','img')