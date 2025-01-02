from django.db import models

# Create your models here.

class User(models.Model):
    url = models.URLField()
    username = models.CharField(max_length=200)
    email = models.EmailField(max_length=200)
    groups = models.CharField(max_length=200)


class MenuItem(models.Model):
    item = models.CharField(max_length=200)
