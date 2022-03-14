from typing import Any
from .logics import DealManager
from apps.apps_htmlapi import BaseHtmlAPI, BaseDetailHtmlAPI


class DealApiView(BaseHtmlAPI):

    def __init__(self, **kwargs: Any) -> None:
        super().__init__(DealManager, None, **kwargs)


class DealDetailApiView(BaseDetailHtmlAPI):

    def __init__(self, **kwargs: Any) -> None:
        super().__init__(DealManager, None, **kwargs)
