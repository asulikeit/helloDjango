from rest_framework import serializers
from apps.peoples.serializers import PeopleSerializer, PeopleListSerializer
from .models import Memberships


class MembershipsSaveSerializer(serializers.ModelSerializer):
    
    class Meta(object):
        model = Memberships
        fields = ('id', 'name', 'description', 'peoples')


class MembershipsSerializer(serializers.ModelSerializer):

    peoples = PeopleListSerializer(read_only=True)
    
    class Meta(object):
        model = Memberships
        fields = ('id', 'name', 'description', 'peoples')


class MembershipsListSerializer(serializers.ModelSerializer):

    peoples = PeopleListSerializer(read_only=True)
    
    class Meta(object):
        model = Memberships
        fields = ('id', 'name', 'peoples')
