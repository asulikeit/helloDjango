from typing import Any

from .logics import PeopleManager
from apps.apps_htmlapi import BaseHtmlAPI, BaseDetailHtmlAPI


class PeopleApiView(BaseHtmlAPI):

    def __init__(self, **kwargs: Any) -> None:
        super().__init__(
            get_key = 'peoples',
            manager = PeopleManager,
            **kwargs)


class PeopleDetailApiView(BaseDetailHtmlAPI):
    
    def __init__(self, **kwargs: Any) -> None:
        super().__init__(PeopleManager, None, **kwargs)
    