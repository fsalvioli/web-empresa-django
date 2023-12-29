
from django.urls import path
from . import views

urlpatterns = [
    # homepage:
    path("", views.contact, name="contact"),
]
