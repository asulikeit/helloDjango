from rest_framework import serializers
from utils.common.strings import copy_by_keys
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
        copy_by_keys(deal_json, instance, 'id')
        deal_json['sender'] = instance.sender.name
        deal_json['receiver'] = instance.receiver.name
        return deal_json
