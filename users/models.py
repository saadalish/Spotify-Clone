from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):

    is_artist = models.BooleanField(default=False)

    def __str__(self):
        return f'{self.first_name} {self.last_name}'
