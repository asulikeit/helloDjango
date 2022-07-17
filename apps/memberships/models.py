from django.db import models
from apps.apps_models import NameAndDescModel
from apps.peoples.models import PeopleModel


class Memberships(NameAndDescModel):
    
    peoples = models.ManyToManyField(PeopleModel, blank=True, related_name='memberships')

    class Meta:
        ordering=['-id']
        