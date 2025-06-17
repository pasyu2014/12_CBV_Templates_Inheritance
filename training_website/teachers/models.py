# teachers/models.py
from django.db import models
from django.contrib.auth.models import AbstractUser, Group, Permission
from django.conf import settings

base_dir = settings.BASE_DIR

class Teacher(AbstractUser):
    bio = models.TextField(blank=True, verbose_name='Биография')
    base_dir = settings.BASE_DIR
    profile_photo = models.ImageField(
        upload_to='base_dir\teachers\photos',
        blank=True, null=True, verbose_name='Фото'
        )

    #teachers/photos/
    def __str__(self):
        return f"{self.get_full_name() or self.username}"



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