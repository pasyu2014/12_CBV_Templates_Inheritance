# users/models.py

from django.contrib.auth.models import AbstractUser, Group, Permission
from django.db import models

class User(AbstractUser):
    is_student = models.BooleanField(default=False, verbose_name='Студент')
    is_teacher = models.BooleanField(default=False, verbose_name='Преподаватель')
    # Можно добавить дополнительные поля по необходимости

    def __str__(self):
        return self.username

    groups = models.ManyToManyField(
        Group,
        related_name='+',
        blank=True,
    )
    user_permissions = models.ManyToManyField(
        Permission,
        related_name='+',
        blank=True,
    )