from django.db import models
from django.db.models import fields
from rest_framework import serializers

from apps.peoples.models import Peoples

class PeopleSerializer(serializers.ModelSerializer):
    class Meta(object):
        model = Peoples
        fields = ('id', 'name', 'description')


class PeopleListSerializer(serializers.ModelSerializer):

    class Meta(object):
        model = Peoples
        fields = ('id', 'name')
