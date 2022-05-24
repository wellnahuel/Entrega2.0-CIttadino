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

class UserEditForm(UserCreationForm):
    email= forms.EmailField(required=True)
    password1= forms.CharField(label="Modificar Contraseña", widget=forms.PasswordInput)
    password2= forms.CharField(label="Confirmar contraseña", widget=forms.PasswordInput)

    last_name= forms.CharField(label="Modificar Apellido")
    first_name= forms.CharField(label="Modificar Nombre")


    class Meta:
        model=User
        fields=('email', 'password1', 'password2', 'last_name', 'first_name')
        help_texts={campito:"" for campito in fields}


class AvatarForm(forms.Form):
    avatar= forms.ImageField(label="Avatar")

