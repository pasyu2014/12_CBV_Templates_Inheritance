# courses/admin.py
from django.contrib import admin

from courses.models import Course

# Register your models here.
@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ('pk', 'title',  'description')
    list_display_links = ('pk', 'title')
