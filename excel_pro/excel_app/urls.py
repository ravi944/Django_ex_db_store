from django.urls import path
from app11 import views

urlpatterns = [
    path('', views.index),
]