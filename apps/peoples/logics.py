from .serializers import PeopleSerializer, PeopleListSerializer
from .models import Peoples

people_serial = PeopleSerializer
people_list_serial = PeopleListSerializer
people_object = Peoples.objects

class PeopleManager:

    def read_one(self, people_number):
        people = people_object.get(id=people_number)
        serial = people_serial(people)
        return serial.data

    def list(self):
        peoples = people_object.all()
        return people_list_serial(peoples, many=True).data

    def create(self, peoples):
        people_numbers = []

        for people in peoples:
            people_number = self.create_one(people)
            people_numbers.append(people_number)

        return people_numbers

    def create_one(self, people):
        serializer = people_serial(data=people)
        serializer.is_valid(raise_exception=True)
        result = serializer.save()
        return result.id
