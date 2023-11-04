from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    eventbrite_token = models.CharField(max_length=255, null=True, blank=True)
