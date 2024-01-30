from django.shortcuts import render,redirect
from django.urls import reverse
from .forms import ContactoForm 
from django.core.mail import EmailMessage
# Create your views here.

def contacto(request):
    contacto_form = ContactoForm()
    if(request.method=='POST'):
        nom = request.POST.get('nombre')
        cor = request.POST.get('correo')
        cont = request.POST.get('contenido')

        #enviar un correo con el mensaje recibido a atencionCliente@miempresa.com
        #crear el objeto para enviar el correo
        emailEnviar = EmailMessage(
            'Nuevo Mnsaje de contacto', #asunto
             f"de {nom}-{cor} \n\n Escribio: \n {cont}",#cuerpo
            "noContestar@miempresa.com",#email de origen
            ["atencionAlCliente@miEmpresa.com"],#lista de email de destino
            reply_to=[cor],#reponder a
            bcc=["atencionAlCliente1@miEmpresa.com","atencionAlCliente2@miEmpresa.com"]
        )
        try:
            emailEnviar.send()
        except Exception as e:
            #manejar errores
            print(f"Error al enviar el correo: {e}")

        contacto_form = ContactoForm(data=request.POST)
        return redirect(reverse('contacto')+'?ok')

    return render(request,"contacto/contacto.html",{'formulario':contacto_form})