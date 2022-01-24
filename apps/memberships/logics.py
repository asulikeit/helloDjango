from .serializers import MembershipsListSerializer, MembershipsSaveSerializer, MembershipsSerializer
from .models import Memberships
from apps.apps_manager import BaseManager


class MembershipManager(BaseManager):

    def __init__(self):        
        self._save_serial = MembershipsSaveSerializer
        self._list_serial = MembershipsListSerializer
        self._serial = MembershipsSerializer
        self._object = Memberships.objects
