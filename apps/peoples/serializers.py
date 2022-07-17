from rest_framework import serializers
from utils.common.strings import copy_by_keys

from utils.security.encrypt_text import decrypt_text, encrypt_text
from .models import PhoneNumber, Profiles, PeopleModel


class ProfileSerializer(serializers.ModelSerializer):
    
    class Meta(object):
        model = Profiles
        fields = ('id', 'profile_info')


class PeopleListSerializer(serializers.ModelSerializer):

    class Meta(object):
        model = PeopleModel
        fields = ('id', 'name')


class PeopleSerializer(serializers.ModelSerializer):

    profile = ProfileSerializer(required=False)
    memberships = serializers.SerializerMethodField('get_memberships_prefetch_related')

    class Meta(object):
        model = PeopleModel
        fields = ('id', 'name', 'description', 'profile', 'memberships')

    def get_memberships_prefetch_related(self, people):
        memberships = people.memberships.all()
        datas = []
        for membership in memberships:
            data = {'id': membership.id, 'name': membership.name}
            datas.append(data)
        return datas
    
    # when serial.data
    def to_representation(self, instance):
        people_json = {}
        copy_by_keys(people_json, instance, 'id', 'name', 'description')

        if instance.profile:
            profile_json = {}
            profile_infos = self._decrypt(instance.name, instance.profile)
            for profile_info in profile_infos.split("+"):
                key_value = profile_info.split(":")
                profile_json[key_value[0]] = key_value[1]
            people_json['profile'] = profile_json
        else:
            people_json['profile'] = {}

        if instance.memberships:
            membership_list = []
            for membership in instance.memberships.all():
                membership_list.append({'id': membership.id, 'name': membership.name})
            people_json['memberships'] = membership_list
        else:
            people_json['memberships'] = {}

        return people_json

    # when is_valid()
    def to_internal_value(self, people_data):
        if people_data.get('profile'):
            profile_info = ""
            profile = people_data.pop('profile')
            for key, value in profile.items():
                rkey = key.replace("+", "").replace(":", "")
                rvalue = value.replace("+", "").replace(":", "")
                profile_info += f"{rkey}:{rvalue}+"
            people_data['profile'] = {'profile_info': profile_info[:-1]}
        return people_data

    # create when save
    def create(self, valid_data):
        people_obj = None
        if valid_data.get('profile'):
            profile_str = self._encrypt(valid_data.get('name'), valid_data.pop('profile'))
            profile_obj = Profiles.objects.create(**profile_str)
            people_obj = PeopleModel.objects.create(profile=profile_obj, **valid_data)
        else:
            people_obj = PeopleModel.objects.create(**valid_data)
        return people_obj

    # update when save
    def update(self, instance, validated_data):
        update_data = super().update(instance, validated_data)
        return update_data

    def _encrypt(self, username, profile):
        encrypt_profile = {}
        for key, value in profile.items():
            encrypt_profile[key] = encrypt_text(value, username)
        return encrypt_profile

    def _decrypt(self, username, encrypt_profile):
        return decrypt_text(encrypt_profile.profile_info, username)


class PhonenumbersSerializer(serializers.ModelSerializer):

    people = PeopleListSerializer()

    class Meta(object):
        model = PhoneNumber
        fields = ('id', 'number', 'people')
