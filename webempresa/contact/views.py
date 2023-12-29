from django.shortcuts import render, redirect
from django.urls import reverse
from .forms import ContactForm
from django.core.mail import EmailMessage
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail
import os
# Create your views here.
def contact(request):
    contact_form = ContactForm()

    if request.method == "POST": # si la petición es POST (y no es GET), entonces recuperamos los datos enviados.
        contact_form = ContactForm(data=request.POST)
        if contact_form.is_valid():
            name = request.POST.get('name', '')
            email = request.POST.get('email', '')
            content = request.POST.get('content', '')
            # Enviamos el correo y redireccionamos: 
            message = Mail(
                from_email='salvioli.franco@gmail.com',
                to_emails='franco.salvioli.work@gmail.com',
                subject="Contact",
                plain_text_content=f"{name} {email}\n\n{content}",
                
            )
            try:
                sg = SendGridAPIClient(os.environ.get('SENDGRID_API_KEY'))
                response = sg.send(message)
                print('Correo enviado con éxito')
                print(response)
            except Exception as e:
                print('Error al enviar el correo:', e)
            
            
            #try:
            #    email.send()
            #    return redirect(reverse('contact')+"?ok")
            #except:
                # error, algo no ha ido bien
            #    return redirect(reverse('contact')+"?fail") # dejamos que Django resuelva el mismo las urls.

    return render(request, 'contact/contact.html', {'form': contact_form})