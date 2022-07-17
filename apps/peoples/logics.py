from typing import List

from apps.peoples.domains import ClubUsers, SignForms
from utils.exception import HelloServerError
from .serializers import PeopleSerializer, PeopleListSerializer, PhonenumbersSerializer
from .models import PeopleModel
from apps.apps_manager import BaseManager


class PeopleManager(BaseManager):
    
    def __init__(self):        
        self._save_serial = PeopleSerializer
        self._list_serial = PeopleListSerializer
        self._serial = PeopleSerializer
        self._object = PeopleModel.objects

    _pnumber_serial = PhonenumbersSerializer

    def add_phonenumbers(self, id, phonenumbers):
        people = PeopleModel.objects.get(id=id)
        for pnumber in phonenumbers:
            people = PeopleModel.objects.get(id=id)
            data = {
                'people': people,
                'number': pnumber,
            }
            serializer = self._pnumber_serial(data=data)
            serializer.is_valid()


class MembersLogic:

    @staticmethod
    def signup(sign_forms: SignForms) -> None:
        request_len = len(sign_forms)
        result_len = 0
        while (sign_forms.is_exist()):
            new_people = ClubUsers(sign_forms.pop())
            WaitingList.instance().add(new_people)
            result_len += 1
        if request_len != result_len:
            raise HelloServerError("Failed to register some users to list.")

    @staticmethod
    def check_waiting() -> List:
        return WaitingList.instance().list()


class SingletonInstane:
    __instance = None
    
    @classmethod
    def __getInstance(cls):
        return cls.__instance
        
    @classmethod
    def instance(cls, *args, **kargs):
        cls.__instance = cls(*args, **kargs)
        cls.instance = cls.__getInstance
        return cls.__instance


class WaitingList(SingletonInstane):

    _list = []

    def add(self, people: ClubUsers):
        self._list.append(people)

    def pop(self):
        if len(self._list) > 0:
            return self._list.pop()
        else:
            return None

    def is_exist(self):
        return len(self._list) > 0

    def __len__(self):
        return len(self._list)

    def list(self):
        return self._list
