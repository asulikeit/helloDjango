from .serializers import DealsSerializer
from .models import Deals

deal_serial = DealsSerializer
deal_object = Deals.objects

class DealManager:

    def make(self, deal_peoples):
        serializer = deal_serial(data=deal_peoples)
        serializer.is_valid(raise_exception=True)
        result = serializer.save()
        return result.id

    def read_one(self, deal_id):
        deal = deal_object.get(id=deal_id)
        return deal_serial(deal).data
