from django.urls import re_path
from . import views

app_name='memberships'

urlpatterns = [
    re_path(r'/?$', views.MembershipApiView.as_view()),
    re_path(r'/(?P<id>[0-9]+)/?$', views.MembershipDetailApiView.as_view()),
]
