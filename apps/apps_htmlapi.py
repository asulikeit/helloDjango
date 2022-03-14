from enum import Enum
from typing import Any
from rest_framework.response import Response
from django.core.exceptions import ObjectDoesNotExist
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.exceptions import ValidationError


class BaseAPIView(APIView):

    def __init__(self, manager, get_key = None, **kwargs: Any) -> None:
        super().__init__(**kwargs)
        self._key = get_key
        self._manager = manager()


class BaseHtmlAPI(BaseAPIView):
    
    default_page = 1
    default_size = 10
        
    def get(self, request):
        page = request.query_params.get('page') or self.default_page
        size = request.query_params.get('size') or self.default_size
        people_list, total_count, total_pages = self._manager.list(page = page, size = size)
        resp_data = {
            'total_count': total_count,
            'total_pages': total_pages,
            'data': people_list
        }
        return Response(status=status.HTTP_200_OK, data=resp_data)

    def post(self, request):
        try:
            if self._key:
                json_list = request.data.get(self._key)
                if (type(json_list) is not list) or len(json_list) <= 0:
                    raise AttributeError('No correct input type. It must be list type.')
                created_ids = self._manager.create(json_list)
                return Response(status=status.HTTP_201_CREATED, data=created_ids)
            else:
                deal_peoples = request.data
                deal_id = self._manager.create_one(deal_peoples)
                return Response(status=status.HTTP_201_CREATED, data=deal_id)
        except KeyError as ke:
            return Response(status=status.HTTP_400_BAD_REQUEST)
        except ( ValidationError, AttributeError ) as ve:
            return Response(status=status.HTTP_400_BAD_REQUEST) 
        except Exception as e:
            return Response(status=444)


class BaseDetailHtmlAPI(BaseAPIView):

    def get(self, request, id):
        try:
            people = self._manager.read(id)
            return Response(status=status.HTTP_200_OK, data=people)
        except KeyError as ke:
            return Response(status=status.HTTP_400_BAD_REQUEST)
        except ObjectDoesNotExist as ne:
            return Response(status=status.HTTP_404_NOT_FOUND)
        except Exception as e:
            return Response(status=444)

    def post(self, request, id):
        try:
            self._manager.update(id, request.data)
            return Response(status=status.HTTP_204_NO_CONTENT)
        except KeyError as ke:
            return Response(status=status.HTTP_400_BAD_REQUEST)
        except ObjectDoesNotExist as ne:
            return Response(status=status.HTTP_404_NOT_FOUND)
        except Exception as e:
            return Response(status=444)
