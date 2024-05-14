from django.db import models


class Device(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class FileType(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name
