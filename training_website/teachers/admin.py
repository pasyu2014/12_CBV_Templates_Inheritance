# teachers/admin.py
from django.contrib import admin

from teachers.models import Teacher

# Register your models here.
@admin.register(Teacher)
class TeacherAdmin(admin.ModelAdmin):
    list_display = ('pk', 'username', 'first_name', 'last_name')
    list_display_links = ('pk', 'username')
