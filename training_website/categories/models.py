# categories/models.py
from django.db import models

# Create your models here.
class Category(models.Model):
    class Meta:
        verbose_name_plural ='Категории'
    name = models.CharField(max_length=100, unique=True, verbose_name='Название категории')
    description = models.TextField(blank=True, verbose_name='Описание')

    def __str__(self):
        return self.name