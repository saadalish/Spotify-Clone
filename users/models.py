from django.contrib.auth.models import User
from django.db import models


class Artist(models.Model):

    user = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        verbose_name_plural = "Artists"

    def __str__(self):
        return f'{self.user}'
