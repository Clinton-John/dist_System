from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.models import User

class Details(models.Model):
    number = models.CharField(max_length=20, blank=True)
    email = models.EmailField()
    address = models.CharField(max_length=255, blank=True)
    reg_no = models.CharField(max_length=50)