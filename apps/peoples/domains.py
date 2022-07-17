from rest_framework import serializers


class SignSerialzer(serializers.Serializer):

    name = serializers.CharField(max_length=200)
    description = serializers.CharField(max_length=999)


class SignForm(object):
    pass


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


class ClubUsersSerialzer(serializers.Serializer):

    name = serializers.CharField(max_length=200)
    description = serializers.CharField(max_length=999)


class ClubUsers:

    def __init__(self, sign_form) -> None:
        pass
