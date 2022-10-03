from apps.apps_htmlapi import SimpleAPIView
from .domains import ClubUserSerialzer, SignForms
from .logics import MembersLogic
from utils.exception import HelloServerError

from rest_framework import status
from rest_framework.response import Response
from rest_framework.exceptions import server_error


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
