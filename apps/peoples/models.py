from django.db import models

class Peoples(models.Model):

    name = models.CharField(max_length=200, unique=True)
    description = models.TextField(blank=True)
