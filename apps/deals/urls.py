from django.urls import path
from . import views

app_name='deals'

urlpatterns = [
    path('', views.DealApiView.as_view()),
    path('<int:id>/', views.DealDetailApiView.as_view()),
]