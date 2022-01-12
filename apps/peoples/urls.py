from django.urls import re_path
from . import views

app_name='peoples'

urlpatterns = [
    re_path(r'/?$', views.PeopleApiView.as_view()),
    re_path(r'/(?P<id>[0-9]+)/?$', views.PeopleDetailApiView.as_view()),
]