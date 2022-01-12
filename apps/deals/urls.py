from django.urls import re_path
from . import views

app_name='deals'

urlpatterns = [
    re_path(r'/?$', views.DealApiView.as_view()),
    re_path(r'/(?P<id>[0-9]+)/?$', views.DealDetailApiView.as_view()),
]