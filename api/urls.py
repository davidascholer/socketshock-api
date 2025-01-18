from django.contrib import admin
from django.urls import path

from api.views import vinyl_view, base_view

urlpatterns = [
    path('', base_view.denied, name="root"),
    path('test/', base_view.test, name="test"),
    path('vinyl/', vinyl_view.vinyl_list, name="vinyl_list"),
    path('vinyl/detail/<str:id>/', vinyl_view.vinyl_detail, name="vinyl_detail"),
]
