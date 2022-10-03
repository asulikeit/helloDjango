from typing import List

from apps.peoples.logics import PeopleManager
from .domains import SignForms, ClubUser
from utils.exception import HelloServerError


class PeopleLogic:

    manager = PeopleManager()

    @classmethod
    def add(cls, club_user: ClubUser):
        return cls.manager.create(club_user.to_dict)


class MembersLogic:

    @staticmethod
    def add_waiting(sign_forms: SignForms) -> None:
        request_len = len(sign_forms)
        result_len = 0
        while (sign_forms.is_exist()):
            new_people = ClubUser(sign_forms.pop())
            WaitingList.instance().add(new_people)
            result_len += 1
        if request_len != result_len:
            #TODO: atomic
            raise HelloServerError("Failed to register some users to list.")

    @staticmethod
    def check_waiting() -> List:
        return WaitingList.instance().list()

    @staticmethod
    def confirm_waiting():
        waiting_users = WaitingList.instance().list()
        for waiting_user in waiting_users:
            test = PeopleLogic.add(waiting_user)
            pass
        pass


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

    def add(self, people: ClubUser):
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
