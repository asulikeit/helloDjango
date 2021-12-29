from rest_framework import serializers
from rest_framework.status import is_redirect

from apps.peoples.serializers import PeopleSerializer
from apps.peoples.models import Peoples

from .models import Deals

class DealsSerializer(serializers.ModelSerializer):
    sender = PeopleSerializer()

    class Meta(object):
        model = Deals
        fields = ('id', 'sender', 'receiver')

    def create(self, validated_data):
        sender_id = validated_data.pop('sender')
        sender = Peoples.objects.get(id=sender_id)
        validated_data['sender'] = sender
        deal = Deals.objects.create(**validated_data)
        return deal