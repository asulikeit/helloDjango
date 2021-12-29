from django.urls import path
from . import views

app_name='peoples'

urlpatterns = [
    path('', views.PeopleApiView.as_view()),
    path('<int:id>/', views.PeopleDetailApiView.as_view()),
]