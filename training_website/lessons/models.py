# lessons/models.py
from django.db import models
from courses.models import Course

class Lesson(models.Model):
    title = models.CharField(max_length=200, verbose_name='Название занятия')
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name='lessons', verbose_name='Курс')
    description = models.TextField(blank=True, verbose_name='Описание')
    date = models.DateTimeField(verbose_name='Дата и время занятия')
    order = models.PositiveIntegerField(default=0, verbose_name='Порядок')

    class Meta:
        ordering = ['order']

    def __str__(self):
        return f"{self.course.title} - {self.title}"

class Schedule(models.Model):
    lesson = models.ForeignKey(Lesson, on_delete=models.CASCADE, related_name='schedules', verbose_name='Занятие')
    date_time = models.DateTimeField(verbose_name='Дата и время')
    location = models.CharField(max_length=255, blank=True, verbose_name='Место проведения')
    duration_minutes = models.PositiveIntegerField()

    class Meta:
        ordering = ['date_time']

    def __str__(self):
        return f"{self.lesson} - {self.date_time}"
    


class Material(models.Model):
    lesson = models.ForeignKey(Lesson, on_delete=models.CASCADE, related_name='materials', verbose_name='Занятие')
    title = models.CharField(max_length=200, verbose_name='Название материала')
    url = models.URLField(verbose_name='Ссылка')
    
    # Определяем choices как переменную вне поля модели
    material_type_choices = [
        ('video', 'Видео (YouTube, Vimeo, Rutube)'),
        ('github', 'GitHub'),
        ('article', 'Статья/Документ'),
        ('other', 'Другое'),
    ]
    
    material_type = models.CharField(
        max_length=20,
        choices=material_type_choices,
        default='other',
        verbose_name='Тип материала'
    )

    def __str__(self):
        max_length = 50  # задайте нужную длину
        lesson_title = self.lesson.title[:max_length]

        if len(self.lesson.title) > max_length:
            lesson_title = lesson_title[:max_length-3] + '...'
        return f"{lesson_title} - {self.title}"

    
    
"""
оставить список `material_type_choices` внутри класса, то его можно объявить как атрибут класса:

```python
class Material(models.Model):
    material_type_choices = [
        ('video', 'Видео (YouTube, Vimeo, Rutube)'),
        ('github', 'GitHub'),
        ('article', 'Статья/Документ'),
        ('other', 'Другое'),
    ]

    lesson = models.ForeignKey(Lesson, on_delete=models.CASCADE, related_name='materials', verbose_name='Занятие')
    title = models.CharField(max_length=200, verbose_name='Название материала')
    url = models.URLField(verbose_name='Ссылка')
    material_type = models.CharField(
        max_length=20,
        choices=material_type_choices,
        default='other',
        verbose_name='Тип материала'
    )
    description = models.TextField(blank=True, verbose_name='Описание')
```
"""
