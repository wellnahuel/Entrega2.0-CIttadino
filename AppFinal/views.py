from dataclasses import fields
from turtle import color
from django.http import HttpResponse
from django.shortcuts import render

from AppFinal.forms import UsuarioForm, AnimalForm, DatosForm

from .models import *

from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

# Create your views here.
def usuario(request):

    if request.method == 'POST':
        formulario=UsuarioForm(request.POST)

        if formulario.is_valid():
            informacion=formulario.cleaned_data
            usuario=Usuario(nombre=informacion['nombre'], apellido=informacion['apellido'], email=informacion['email'], celular=informacion['celular'])
            usuario.save()
            return render(request, "AppFinal/inicio.html")

    else: 
        formulario=UsuarioForm()
        return render(request, "AppFinal/usuarios.html", {'formulario':formulario})
        
    return render(request, "AppFinal/usuarios.html")

def animal(request):

    if request.method == 'POST':
        formularioanimal=AnimalForm(request.POST)

        if formularioanimal.is_valid():
            infoanimal=formularioanimal.cleaned_data
            animal=Animal(raza=infoanimal['raza'], color=infoanimal['color'])
            animal.save()
            return render(request, "AppFinal/inicio.html")

        else: 
            formularioanimal=AnimalForm()
            return render(request, "AppFinal/animal.html", {'formularioanimal':formularioanimal})

    return render(request, "AppFinal/animal.html")

def datos(request):

    if request.method == 'POST':
        formulariodatos=DatosForm(request.POST)

        if formulariodatos.is_valid():
            infodatos=formulariodatos.cleaned_data
            datos=Datos(fecha=infodatos['fecha'], lugar=infodatos['lugar'], condicion=infodatos['condicion'])
            datos.save()
            return render(request, "AppFinal/datos.html")

        else: 
            formulariodatos=DatosForm()
            return render(request, "AppFinal/datos.html", {'formulariodatos':formulariodatos})

    return render(request, "AppFinal/datos.html")

def inicio(request):
    return render(request, "AppFinal/inicio.html")



def buscarUsuario(request):

    if request.GET['apellido']:
        apellido=request.GET['apellido']
        usuarios=Usuario.objects.filter(apellido__icontains=apellido)
        return render(request, "AppFinal/resultadoBU.html", {'usuarios':usuarios})
    else:
        respuesta="No se ingreso ningun apellido"
        return render(request, "AppFinal/resultadoBU.html", {'respuesta':respuesta})


def leerUsuarios(request):
    usuarios = Usuario.objects.all() #trae todos los usuarios
    contexto = {"usuarios":usuarios}
    print(contexto)
    return render(request, "AppFinal/leerUsuarios.html", contexto)

def eliminarUsuario(request, nombre):
    usuario=Usuario.objects.get(nombre=nombre)
    usuario.delete()
    usuarios=Usuario.objects.all()
    contexto={'usuarios':usuarios}

    return render(request, 'AppFinal/leerUsuarios.html', contexto)

def editarUsuario(request, nombre):
    usuario=Usuario.objects.get(nombre=nombre)
    if request.method == 'POST':
        formulario=UsuarioForm(request.POST)
        if formulario.is_valid():
            informacion=formulario.cleaned_data
            usuario.nombre=informacion['nombre']
            usuario.apellido=informacion['apellido']
            usuario.email=informacion['email']
            usuario.celular=informacion['celular']
            usuario.save()
            #luego muestro la listade usuarios de nuevo
            usuarios=Usuario.objects.all()
            contexto={'usuarios':usuarios}

            return render(request, 'AppFinal/leerUsuarios.html', contexto)

    else:
        formulario=UsuarioForm(initial={'nombre':usuario.nombre, 'apellido':usuario.apellido, 'email':usuario.email, 'celular':usuario.celular})
        return render(request, 'AppFinal/editarUsuario.html', {'formulario':formulario, 'nombre':nombre})
    
#---------------------------------------------------------------------

class AnimalesList(ListView):
    model = Animal
    template_name = 'AppFinal/animal.html'

class AnimalDetalle(DetailView):
    model = Animal
    template_name = 'AppFinal/animalDetalle.html'

class AnimalCreacion(CreateView):
    model = Animal
    success_url = reverse_lazy('animal_listar')
    fields = ['raza', 'color']

class AnimalEdicion(UpdateView):
    model = Animal
    success_url = reverse_lazy('animal_listar')
    fields = ['raza', 'color']

class AnimalEliminacion(DeleteView):
    model = Animal
    success_url = reverse_lazy('animal_listar')
    fields = ['raza', 'color']






