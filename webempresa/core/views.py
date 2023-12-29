from django.shortcuts import render, HttpResponse
from django.core.mail import send_mail
# Create your views here.


def index(request):
    # Lógica de la página de inicio
    return render(request, 'core/index.html')

def about(request):

    return render(request, 'core/about.html')

def store(request):

    return render(request, 'core/store.html')