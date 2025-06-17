#categories/admin.py
from django.contrib import admin
from categories.models import Category

# Register your models here.
@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('pk', 'name',  'description')
    list_display_links = ('pk', 'name')