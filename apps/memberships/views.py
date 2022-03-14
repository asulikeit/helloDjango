from typing import Any
from apps.apps_htmlapi import BaseHtmlAPI, BaseDetailHtmlAPI
from .logics import MembershipManager


class MembershipApiView(BaseHtmlAPI):

    def __init__(self, **kwargs: Any) -> None:
        super().__init__(
            get_key = 'memberships',
            manager = MembershipManager,
            **kwargs)


class MembershipDetailApiView(BaseDetailHtmlAPI):

    def __init__(self, **kwargs: Any) -> None:
        super().__init__(MembershipManager, None, **kwargs)
