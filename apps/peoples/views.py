from typing import Any

from apps.peoples.domains import ClubUsersSerialzer, SignForms
from utils.exception import HelloServerError
from .logics import MembersLogic, PeopleManager
from apps.apps_htmlapi import BaseHtmlAPI, BaseDetailHtmlAPI, SimpleAPIView

from rest_framework import status
from rest_framework.response import Response
from rest_framework.exceptions import server_error


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


class PeopleHttpApi(SimpleAPIView):

    def post(self, request):
        try:
            self.check_request_data(request, 'peoples')
            peoples = request.data['peoples']
            new_sign_forms = SignForms(peoples)
            MembersLogic.signup(new_sign_forms)
            return Response(status=status.HTTP_201_CREATED)
        except HelloServerError as hse:
            self.logger.error(hse.args[0])
            return server_error(request)

    def get(self, request):
        try:
            waiting_user_list = MembersLogic.check_waiting()
            serial = ClubUsersSerialzer(waiting_user_list, many=True)
            resp_data = serial.data
            return Response(status=status.HTTP_200_OK, data=resp_data)
        except HelloServerError as hse:
            self.logger.error(hse.args[0])
            return server_error(request)
