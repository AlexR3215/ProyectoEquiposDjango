from django import forms
from django.contrib.auth.forms import UserCreationForm 
from django.contrib.auth.models import User

#Heredar del formulario predefinido de django que nos da 3 campos(nombre,contraseña y confirmarContraseña)
class FormlarioRegistroConCorreo(UserCreationForm):
    email = forms.EmailField(required=True,help_text='Obligatorio, 254 caracteres maximo y valido')

    class Meta:
        model = User
        fields = ('username','email','password1','password2')

    #obtener el correo de la base de dartos y comprobar si existe
    #si existe devolver un error porque ya esta registrado
    def clean_email(self):
        correo = self.cleaned_data.get('email')
        if User.objects.filter(email=correo).exists:
            raise forms.ValidationError("El mail ya esta registrado")
        return correo
        