from django.db import models

from apps.peoples.models import PeopleModel

class Deals(models.Model):

    sender = models.ForeignKey(PeopleModel, on_delete=models.DO_NOTHING, related_name='sender', unique=False)
    receiver = models.ForeignKey(PeopleModel, on_delete=models.DO_NOTHING, related_name='receiver', unique=False)

    class Meta:
        ordering = ['-id']
