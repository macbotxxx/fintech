from django.contrib import admin
from .models import Blog, My_Cars
# Register your models here.

@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
    pass

@admin.register(My_Cars)
class My_CarsAdmin(admin.ModelAdmin):
    list_display = ('car_name', 'price_tag', 'gear', 'door', 'color', 'spear_tyre')
    list_filter = ('car_name', 'price_tag', 'gear')