from rest_framework import serializers
from rest_framework.status import is_redirect

from apps.peoples.serializers import PeopleSerializer
from apps.peoples.models import Peoples

from .models import Deals


class DealsSaveSerializer(serializers.ModelSerializer):
    
    class Meta(object):
        model = Deals
        fields = ('id', 'sender', 'receiver')


class DealsSerializer(serializers.ModelSerializer):
    sender = PeopleSerializer(read_only=True)
    receiver = PeopleSerializer(read_only=True)

    class Meta(object):
        model = Deals
        fields = ('id', 'sender', 'receiver')
