from rest_framework import serializers
from apps.peoples.serializers import PeopleListSerializer
from .models import Memberships


class MembershipsSaveSerializer(serializers.ModelSerializer):
    
    class Meta(object):
        model = Memberships
        fields = ('id', 'name', 'description', 'peoples')


class MembershipsSerializer(serializers.ModelSerializer):

    # peoples = PeopleListSerializer(read_only=True)
    peoples = serializers.SerializerMethodField('get_peoples_prefech_related')
    
    class Meta(object):
        model = Memberships
        fields = ('id', 'name', 'description', 'peoples')

    def get_peoples_prefech_related(self, membership):
        peoples = membership.peoples.all()
        datas = []
        for people in peoples:
            data = {'id': people.id, 'name': people.name}
            datas.append(data)
        return datas


class MembershipsListSerializer(serializers.ModelSerializer):

    peoples = PeopleListSerializer(read_only=True)
    
    class Meta(object):
        model = Memberships
        fields = ('id', 'name', 'peoples')
