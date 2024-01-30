from django import forms


class ContactoForm(forms.Form):
    nombre = forms.CharField(label="Nombre", required=True,widget=forms.TextInput(
        attrs={'class':'form-control'}
    ))
    correo = forms.EmailField(label="Correo",required=True,widget=forms.EmailInput(
        attrs={'class':'form-control','id':'miIdCorreo', 'value':'mail@mail.com'}
    ))
    contenido = forms.CharField(label="Contenido", required=True,widget=forms.Textarea(
        attrs={'class':'form-control','placeholder':'Escriba aqui su mensaje'}
    ),min_length=10,max_length=200)