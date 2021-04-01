import random
import string

from django.contrib.auth.models import AbstractUser
from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models

from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token


@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_auth_token(instance=None, created=False, **kwargs):
    if created:
        Token.objects.create(user=instance)


class CustomUser(AbstractUser):

    email = models.EmailField(blank=True, null=True)

    def __str__(self):
        return str(self.email)
