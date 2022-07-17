from django.db import models
from apps.apps_models import NameAndDescModel

class Profiles(models.Model):

    profile_info = models.JSONField(default=None)


class PeopleModel(NameAndDescModel):
    
    profile = models.OneToOneField(Profiles, on_delete=models.CASCADE, blank=True, null=True)

    class Meta:
        ordering=['-id']


class PhoneNumber(models.Model):

    people = models.ForeignKey(PeopleModel, on_delete=models.CASCADE)
    number = models.CharField(max_length=20, blank=False, unique=True)
