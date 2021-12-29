from django.db import models

from apps.peoples.models import Peoples

class Deals(models.Model):

    sender = models.OneToOneField(Peoples, on_delete=models.DO_NOTHING, related_name='sender')
    receiver = models.OneToOneField(Peoples, on_delete=models.DO_NOTHING, related_name='receiver')
