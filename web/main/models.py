from django.db import models

# Create your models here.


class Book(models.Model):
    name = models.CharField(max_length=100)
    content = models.TextField(blank=True)
    photo = models.URLField(max_length=200)
    author = models.TextField(blank=True)

    def __str__(self):
        return self.name


class User(models.Model):
    name = models.CharField(max_length=50)
    surname = models.CharField(max_length=50)
    log = models.CharField(max_length=50)
    pas = models.CharField(max_length=50)

