from typing import Any

from .logics import PeopleManager
from apps.apps_htmlapi import BaseHtmlAPI, BaseDetailHtmlAPI, SimpleAPIView

from rest_framework import status
from rest_framework.response import Response


class PeopleApiView(BaseHtmlAPI):

    def __init__(self, **kwargs: Any) -> None:
        super().__init__(
            get_key = 'peoples',
            manager = PeopleManager,
            **kwargs)


class PeopleDetailApiView(BaseDetailHtmlAPI):
    
    def __init__(self, **kwargs: Any) -> None:
        super().__init__(PeopleManager, None, **kwargs)


class PNumbersApiView(SimpleAPIView):

    _manager = PeopleManager()
    
    def post(self, request, id):
        self.check_request_data(request, 'phonenumbers')
        phonenumbers = request.data['phonenumbers']
        self._manager.add_phonenumbers(id, phonenumbers)
        if len(phonenumbers) == 2:
            return Response(status=status.HTTP_201_CREATED)
