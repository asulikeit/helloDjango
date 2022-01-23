from .serializers import DealsListSerializer, DealsSerializer, DealsSaveSerializer
from .models import Deals
from apps.apps_manager import BaseManager


class DealManager(BaseManager):

    def __init__(self):        
        self._save_serial = DealsSaveSerializer
        self._list_serial = DealsListSerializer
        self._serial = DealsSerializer
        self._object = Deals.objects
