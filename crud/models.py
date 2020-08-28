from django.db import models

# Create your models here.


class User(models.Model):
    fullName = models.CharField(max_length=200)
    email = models.CharField(max_length=20)
    password = models.CharField(max_length=6)
