from django.db import models
from apps.apps_models import NameAndDescModel
from apps.peoples.models import Peoples


class Memberships(NameAndDescModel):
    
    peoples = models.ManyToManyField(Peoples, blank=True)
