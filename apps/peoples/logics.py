from .serializers import PeopleSerializer, PeopleListSerializer
from .models import Peoples


class PeopleManager:
    
    def __init__(self):        
        self._save_serial = PeopleSerializer
        self._list_serial = PeopleListSerializer
        self._serial = PeopleSerializer
        self._object = Peoples.objects

    def read_one(self, people_number):
        people = self._object.get(id=people_number)
        return self._serial(people).data

    def list(self):
        peoples = self._object.all()
        return self._list_serial(peoples, many=True).data

    def create(self, peoples):
        people_numbers = []

        for people in peoples:
            people_number = self.create_one(people)
            people_numbers.append(people_number)

        return people_numbers

    def create_one(self, people):
        serializer = self._save_serial(data=people)
        serializer.is_valid(raise_exception=True)
        result = serializer.save()
        return result.id
