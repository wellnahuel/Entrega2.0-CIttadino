from django import forms
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth.models import User



class UsuarioForm(forms.Form):
    nombre= forms.CharField(max_length=30)
    apellido= forms.CharField(max_length=30)
    email= forms.EmailField(max_length=40)
    celular= forms.IntegerField()

class AnimalForm(forms.Form):
    raza= forms.CharField(max_length=30)
    color= forms.CharField(max_length=30)

class DatosForm(forms.Form):
    fecha = forms.DateField()  
    lugar= forms.CharField(max_length=30)
    condicion= forms.CharField(max_length=30)

class UserRegistrationForm(UserCreationForm):
    email = forms.EmailField(required=True)
    password1 = forms.CharField(label="Contraseña", widget=forms.PasswordInput)
    password2 = forms.CharField(label="Confirmar Contraseña", widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')
        help_texts={ k:"" for k in fields }


