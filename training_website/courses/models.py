# courses/models.py
from django.db import models
from categories.models import Category
from teachers.models import Teacher

class Course(models.Model):
    title = models.CharField(max_length=200, verbose_name='Название курса')
    description = models.TextField(blank=True, verbose_name='Описание курса')
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, related_name='courses', verbose_name='Категория')
    teachers = models.ManyToManyField(Teacher, related_name='courses', verbose_name='Преподаватели')
    start_date = models.DateField(null=True, blank=True, verbose_name='Дата начала')
    end_date = models.DateField(null=True, blank=True, verbose_name='Дата окончания')
    image = models.ImageField(upload_to='courses/images/', blank=True, null=True, verbose_name='Изображение')

    def __str__(self):
        return self.title
