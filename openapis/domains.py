from re import L
from rest_framework import serializers


class SignSerialzer(serializers.Serializer):

    name = serializers.CharField(max_length=100)
    description = serializers.CharField(max_length=200)


class SignForm:
    name = ''
    description = ''


class SignForms:

    _form = SignSerialzer
    _data = []

    def __init__(self, sign_info) -> None:
        serial = self._form(data=sign_info, many=True)
        serial.is_valid(raise_exception=True)
        for dist_one in serial.data:
            sign_form = SignForm()
            for key, value in dist_one.items():
                setattr(sign_form, key, value)
            self._data.append(sign_form)

    def pop(self):
        if len(self._data) > 0:
            return self._data.pop()
        else:
            return None

    def is_exist(self):
        return len(self._data) > 0

    def __len__(self):
        return len(self._data)


class ClubUserSerialzer(serializers.Serializer):

    name = serializers.CharField(max_length=200)
    description = serializers.CharField(max_length=999)


class ClubUser:

    _serial = ClubUserSerialzer

    def __init__(self, sign_form) -> None:
        sign_form_dict = SignSerialzer(sign_form).data
        serial = self._serial(data=sign_form_dict)
        serial.is_valid(raise_exception=True)
        dist_one = serial.data
        for key, value in dist_one.items():
            setattr(self, key, value)

    def to_dict(self) -> dict:
        return self._serial(self).data
