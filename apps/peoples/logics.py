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
