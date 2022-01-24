from typing import Any
from apps.apps_htmlapi import BaseHtmlAPI
from .logics import MembershipManager


class MembershipApiView(BaseHtmlAPI):

    def __init__(self, **kwargs: Any) -> None:
        super().__init__(MembershipManager, **kwargs)
    
    def get(self, request):
        return self.list()

    def post(self, request):
        return self.create(request.data, 'memberships')


class MembershipDetailApiView(BaseHtmlAPI):

    def __init__(self, **kwargs: Any) -> None:
        super().__init__(MembershipManager, **kwargs)

    def get(self, request, id):
        return self.read_one(id)
