# coding: utf-8
from django.db import models
from django.contrib.auth.models import AbstractUser


class CustomUser(AbstractUser):
    """This model override the 'django user model' that we can work on it"""
    surname = models.CharField(max_length=100, null=False, blank=False)
    name = models.CharField(max_length=100, null=False, blank=False)
    email = models.EmailField(max_length=50, null=False, blank=False)
    password1 = models.CharField(max_length=15, null=False, blank=False)
    password2 = models.CharField(max_length=15, null=False, blank=False)
    date_of_birth = models.DateField(default=None, null=True)

    def __str__(self):
        return self.surname
