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
        return self.create(request.data, 'peoples')


class PeopleDetailApiView(BaseHtmlAPI):
    
    def __init__(self, **kwargs: Any) -> None:
        super().__init__(PeopleManager, **kwargs)
    
    def get(self, request, id):
        return self.read_one(id)
