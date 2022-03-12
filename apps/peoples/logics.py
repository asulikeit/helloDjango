from functools import partial
from .serializers import PeopleSerializer, PeopleListSerializer
from .models import Peoples
from apps.apps_manager import BaseManager


class PeopleManager(BaseManager):
    
    def __init__(self):        
        self._save_serial = PeopleSerializer
        self._list_serial = PeopleListSerializer
        self._serial = PeopleSerializer
        self._object = Peoples.objects

    def update(self, obj_id, data):
        origin_people = self._object.get(id=obj_id)
        serializer = self._save_serial(origin_people, data=data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        