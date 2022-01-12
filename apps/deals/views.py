from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from .logics import DealManager

manager = DealManager()

class DealApiView(APIView):

    def post(self, request):
        # request.data.get('')
        try:
            deal_peoples = request.data
            deal_id = manager.make(deal_peoples)
            return Response(status=status.HTTP_201_CREATED, data=deal_id)
        except KeyError as ke:
            return Response(status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response(status=444)

class DealDetailApiView(APIView):

    def get(self, request, id):
        # request.query_params.get('')
        try:
            deal = manager.read_one(id)
            return Response(status=status.HTTP_200_OK, data=deal)
        except KeyError as e:
            return Response(status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response(status=444)
