from django.shortcuts import render, HttpResponse
from django.core.mail import send_mail
from .models import Service
# Create your views here.

def services(request):
    services = Service.objects.all()
    return render(request, 'services/services.html', {'services': services})