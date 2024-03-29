from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView
from django import forms
from .forms import FormlarioRegistroConCorreo
# Create your views here.


class Registro(CreateView):
    form_class = FormlarioRegistroConCorreo
    template_name = 'registration/registro.html'
    success_url = reverse_lazy("inicio")

    def get_success_url(self) -> str:
        return reverse_lazy('login') + "?registroOK"
    
    #funcion para modificar campos del formulario
    def get_form(self,form_class = None):
        form = super(Registro,self).get_form()


        form.fields['username'].widget = forms.TextInput(attrs={'class':'form-control mb-2', 'placeholder':'Nombre de usuario'})
        form.fields['email'].widget = forms.EmailInput(attrs={'class':'form-control mb-2', 'placeholder':'Ecibe el correo'})
        form.fields['password1'].widget = forms.PasswordInput(attrs={'class':'form-control mb-2', 'placeholder':'Contraseña'})
        form.fields['password2'].widget = forms.PasswordInput(attrs={'class':'form-control mb-2', 'placeholder':'Contraseña (confirmar)'})

        for fieldname in ['username','email','password1','password2']:
            form.fields[fieldname].label = ""
        
        return form