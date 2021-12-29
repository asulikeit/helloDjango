from django.core.exceptions import ObjectDoesNotExist
from rest_framework.exceptions import ValidationError
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from .logics import PeopleManager

manager = PeopleManager()

class PeopleApiView(APIView):
    def get(self, request):
        people_list = manager.list()
        return Response(status=status.HTTP_200_OK, data=people_list)

    def post(self, request):
        try:
            peoples = request.data.get('peoples')
            if (type(peoples) is not list) or len(peoples) <= 0:
                raise AttributeError('no correct input type')
            people_numbers = manager.create(peoples)
            return Response(status=status.HTTP_201_CREATED, data=people_numbers)
        except ( ValidationError, AttributeError ) as ve:
            return Response(status=status.HTTP_400_BAD_REQUEST) 
        except Exception as e:
            return Response(status=444)

class PeopleDetailApiView(APIView):
    def get(self, request, id):
        try:
            people = manager.read_one(id)
            return Response(status=status.HTTP_200_OK, data=people)
        except ObjectDoesNotExist as ne:
            return Response(status=status.HTTP_404_NOT_FOUND)
        except Exception as e:
            return Response(status=444)
