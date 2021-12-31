from django.db import models

from apps.peoples.models import Peoples

class Deals(models.Model):

    sender = models.ForeignKey(Peoples, on_delete=models.DO_NOTHING, related_name='sender', unique=False)
    receiver = models.ForeignKey(Peoples, on_delete=models.DO_NOTHING, related_name='receiver', unique=False)
