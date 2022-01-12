from django.db import models

class Profiles(models.Model):

    profile_info = models.JSONField(default=None)


class Peoples(models.Model):

    name = models.CharField(max_length=200, unique=True)
    description = models.TextField(blank=True)
    profile = models.OneToOneField(Profiles, on_delete=models.CASCADE, blank=True, null=True)
