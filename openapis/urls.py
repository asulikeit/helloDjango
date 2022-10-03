from django.urls import re_path
from . import views

app_name='peoples'

urlpatterns = [
    re_path(r'signup/?$', views.PeopleHttpApi.as_view()),
    re_path(r'signup/confirm/?$', views.PeopleConfirmHttpApi.as_view()),
]