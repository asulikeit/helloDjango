from rest_framework import serializers

from apps.peoples.serializers import PeopleSerializer
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


class DealsListSerializer(serializers.ModelSerializer):
    
    sender = PeopleSerializer(read_only=True)
    receiver = PeopleSerializer(read_only=True)

    class Meta(object):
        model = Deals
        fields = ('id', 'sender', 'receiver')
    
    def to_representation(self, instance):
        deal_json = {}
        deal_json['id'] = instance.id
        deal_json['sender'] = instance.sender.name
        deal_json['receiver'] = instance.receiver.name
        return deal_json
