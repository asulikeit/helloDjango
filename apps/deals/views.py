from typing import Any
from .logics import DealManager
from apps.apps_htmlapi import BaseHtmlAPI


class DealApiView(BaseHtmlAPI):

    def __init__(self, **kwargs: Any) -> None:
        super().__init__(DealManager, **kwargs)

    def get(self, request):
        return self.list()

    def post(self, request):
        return self.create_one(request.data)

class DealDetailApiView(BaseHtmlAPI):

    def __init__(self, **kwargs: Any) -> None:
        super().__init__(DealManager, **kwargs)

    def get(self, request, id):
        return self.read_one(id)
