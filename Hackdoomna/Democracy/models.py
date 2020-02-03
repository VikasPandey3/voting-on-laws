from django.db import models
from django.contrib.auth.models import AbstractUser


class CustomUserModel(AbstractUser):
    pass

    def __str__(self):
        return self.username


class Vote(models.Model):
    voter = models.CharField(max_length=12)
    law_code = models.IntegerField(default=0)
    opinion = models.CharField(max_length=5)
    comment = models.TextField(default="comment here")

    def __str__(self):
        return self.voter


