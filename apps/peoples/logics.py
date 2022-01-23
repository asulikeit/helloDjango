from .serializers import PeopleSerializer, PeopleListSerializer
from .models import Peoples
from apps.apps_manager import BaseManager


class PeopleManager(BaseManager):
    
    def __init__(self):        
        self._save_serial = PeopleSerializer
        self._list_serial = PeopleListSerializer
        self._serial = PeopleSerializer
        self._object = Peoples.objects
