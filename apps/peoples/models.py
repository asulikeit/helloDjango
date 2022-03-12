from django.db import models
from apps.apps_models import NameAndDescModel

class Profiles(models.Model):

    profile_info = models.JSONField(default=None)


class Peoples(NameAndDescModel):
    
    profile = models.OneToOneField(Profiles, on_delete=models.CASCADE, blank=True, null=True)
