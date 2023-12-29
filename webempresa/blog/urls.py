from django.urls import path
from . import views

urlpatterns = [
    # homepage:
    path("", views.blog, name="blog"),
    path('category/<int:category_id>/', views.category, name="category"), # category_id es siempre un string, hay que forzar a que sea entero.
]