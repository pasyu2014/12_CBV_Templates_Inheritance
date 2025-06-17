# lessons/admin.py
from django.contrib import admin

from lessons.models import Lesson, Schedule, Material

# Register your models here.
@admin.register(Lesson)
class lessonAdmin(admin.ModelAdmin):
    list_display = ('pk', 'title', 'course', 'description')
    list_display_links = ('pk', 'title')


# Register your models here.
@admin.register(Schedule)
class ScheduleAdmin(admin.ModelAdmin):
    list_display = ('pk', 'lesson', 'date_time')
    list_display_links = ('date_time', 'pk')

# Register your models here.
@admin.register(Material)
class MaterialAdmin(admin.ModelAdmin):
    list_display = ('pk', 'short_lesson', 'title', 'url')
    list_display_links = ('pk', 'short_lesson')
    
    def short_lesson(self, obj):
        # Задайте максимальную длину
        max_length = 50
        lesson_title = obj.lesson.title
        if len(lesson_title) > max_length:
            return lesson_title[:max_length - 3] + '...'
        return lesson_title
    short_lesson.short_description = 'Lesson'