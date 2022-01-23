from typing import Any
from rest_framework.exceptions import ValidationError
from rest_framework.response import Response
from rest_framework import status
from .logics import PeopleManager
from apps.apps_htmlapi import BaseHtmlAPI


class PeopleApiView(BaseHtmlAPI):

    def __init__(self, **kwargs: Any) -> None:
        super().__init__(PeopleManager, **kwargs)

    def get(self, request):
        return self.list()

    def post(self, request):
        try:
            peoples = request.data.get('peoples')
            if (type(peoples) is not list) or len(peoples) <= 0:
                raise AttributeError('no correct input type')
        except ( ValidationError, AttributeError ) as ve:
            return Response(status=status.HTTP_400_BAD_REQUEST) 
        return self.create(peoples)


class PeopleDetailApiView(BaseHtmlAPI):
    
    def __init__(self, **kwargs: Any) -> None:
        super().__init__(PeopleManager, **kwargs)
    
    def get(self, request, id):
        return self.read_one(id)
