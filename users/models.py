from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    username = models.CharField(max_length=30, unique=True)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=128)

    groups = models.ManyToManyField(
        'auth.Group',
        related_name='user_set_custom',
        related_query_name='user_custom',
        blank=True,
        help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.',
    )
    user_permissions = models.ManyToManyField(
        'auth.Permission',
        related_name='user_set_custom',
        related_query_name='user_custom',
        blank=True,
        help_text='Specific permissions for this user.',
    )