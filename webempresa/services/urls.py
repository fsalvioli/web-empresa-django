
from django.urls import path
from . import views

urlpatterns = [
    # services:
    path("", views.services, name="services"),
]