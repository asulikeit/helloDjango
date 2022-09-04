from typing import Any

from apps.peoples.domains import ClubUserSerialzer, SignForms
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
            peoples = request.data.get('peoples')
            new_sign_forms = SignForms(peoples)
            MembersLogic.add_waiting(new_sign_forms)
            return Response(status=status.HTTP_201_CREATED)
        except HelloServerError as hse:
            self.logger.error(hse.args[0])
            return server_error(request)

    def get(self, request):
        try:
            waiting_user_list = MembersLogic.check_waiting()
            serial = ClubUserSerialzer(waiting_user_list, many=True)
            return Response(status=status.HTTP_200_OK, data=serial.data)
        except HelloServerError as hse:
            self.logger.error(hse.args[0])
            return server_error(request)


class PeopleConfirmHttpApi(SimpleAPIView):
    
    #TODO: Admin permission
    def post(self, request):
        MembersLogic.confirm_waiting()
        return Response(status=status.HTTP_201_CREATED)
