from typing import Any
from rest_framework.response import Response
from django.core.exceptions import ObjectDoesNotExist
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.exceptions import ValidationError


class BaseHtmlAPI(APIView):

    def __init__(self, manger, **kwargs: Any) -> None:
        super().__init__(**kwargs)
        self._manager = manger()

    def read_one(self, id):
        try:
            people = self._manager.read_one(id)
            return Response(status=status.HTTP_200_OK, data=people)
        except KeyError as ke:
            return Response(status=status.HTTP_400_BAD_REQUEST)
        except ObjectDoesNotExist as ne:
            return Response(status=status.HTTP_404_NOT_FOUND)
        except Exception as e:
            return Response(status=444)

    def list(self):
        people_list = self._manager.list()
        return Response(status=status.HTTP_200_OK, data=people_list)

    def create(self, req_data, get_key):
        try:
            json_list = req_data.get(get_key)
            if (type(json_list) is not list) or len(json_list) <= 0:
                raise AttributeError('No correct input type. It must be list type.')
            created_ids = self._manager.create(json_list)
            return Response(status=status.HTTP_201_CREATED, data=created_ids)
        except KeyError as ke:
            return Response(status=status.HTTP_400_BAD_REQUEST)
        except ( ValidationError, AttributeError ) as ve:
            return Response(status=status.HTTP_400_BAD_REQUEST) 
        except Exception as e:
            return Response(status=444)

    def create_one(self, request_data):
        try:
            deal_peoples = request_data
            deal_id = self._manager.create_one(deal_peoples)
            return Response(status=status.HTTP_201_CREATED, data=deal_id)
        except KeyError as ke:
            return Response(status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response(status=444)