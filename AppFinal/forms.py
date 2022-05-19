from django import forms

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


