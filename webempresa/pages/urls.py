from django.urls import path
from . import views

urlpatterns = [
    # homepage:
    #path("", views.blog, name="pages"),
    path('<int:page_id>/<slug:page_slug>/', views.page, name="page"), # category_id es siempre un string, hay que forzar a que sea entero.
]