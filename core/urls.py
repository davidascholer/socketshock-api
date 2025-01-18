from django.contrib import admin
from django.urls import path

from core import views

urlpatterns = [
    path('', views.denied, name="core"),
    path('test/', views.test, name="test"),
]
