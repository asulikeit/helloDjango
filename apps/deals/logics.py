from .serializers import DealsListSerializer, DealsSerializer, DealsSaveSerializer
from .models import Deals


class DealManager:

    def __init__(self):        
        self._save_serial = DealsSaveSerializer
        self._list_serial = DealsListSerializer
        self._serial = DealsSerializer
        self._object = Deals.objects

    def read_one(self, deal_id):
        deal = self._object.get(id=deal_id)
        return self._serial(deal).data

    def list(self):
        deals = self._object.all()
        return self._list_serial(deals, many=True).data

    def create(self, deals):
        # TODO
        pass

    def create_one(self, deal_peoples):
        serializer = self._save_serial(data=deal_peoples)
        serializer.is_valid(raise_exception=True)
        result = serializer.save()
        return result.id
