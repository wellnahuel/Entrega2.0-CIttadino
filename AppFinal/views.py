from dataclasses import fields
from turtle import color
from django.http import HttpResponse
from django.shortcuts import render

from AppFinal.forms import UsuarioForm, AnimalForm, DatosForm, UserRegistrationForm, UserEditForm, AvatarForm

from .models import Usuario, Animal, Datos, Avatar

from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User



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

    avatar=Avatar.objects.filter(user=request.user)
    return render(request, "AppFinal/inicio.html", {'url': avatar[0].avatar.url})



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

class AnimalesList(LoginRequiredMixin, ListView):
    model = Animal
    template_name = 'AppFinal/animal.html'

class AnimalDetalle(LoginRequiredMixin, DetailView):
    model = Animal
    template_name = 'AppFinal/animalDetalle.html'

class AnimalCreacion(LoginRequiredMixin, CreateView):
    model = Animal
    success_url = reverse_lazy('animal_listar')
    fields = ['raza', 'color']

class AnimalEdicion(LoginRequiredMixin, UpdateView):
    model = Animal
    success_url = reverse_lazy('animal_listar')
    fields = ['raza', 'color']

class AnimalEliminacion(LoginRequiredMixin, DeleteView):
    model = Animal
    success_url = reverse_lazy('animal_listar')
    fields = ['raza', 'color']


#------------------------LOGIN-------------------------------


def login_request(request):
    if request.method == 'POST':
        formulario = AuthenticationForm(request, data=request.POST)
        if formulario.is_valid():
            usuario=formulario.cleaned_data.get('username')
            clave=formulario.cleaned_data.get('password')

            user=authenticate(username=usuario, password=clave)

            if user is not None:
                login(request, user)
                return render(request, 'AppFinal/inicio.html', {'usuario':usuario, 'mensaje':'Bienvenido al sistema'})

            else: 
                return render(request, 'AppFinal/inicio.html', {'mensaje':'USUARIO INCORRECTO'})
        else:
            return render(request, 'AppFinal/inicio.html', {'mensaje':'FORMULARIO INVALIDO'})
    else:
        formulario=AuthenticationForm()
        return render(request, 'AppFinal/login.html', {'formulario':formulario})

#----------------------------Register----------------------

def register(request):
    if request.method == 'POST':
        formulario = UserRegistrationForm(request.POST)
        if formulario.is_valid():
            username=formulario.cleaned_data['username']
            formulario.save()
            return render(request, 'AppFinal/inicio.html', {'mensaje': f'Usuario: {username} Creado exitosamente'})
        else: 
            return render(request, 'AppFinal/inicio.html', {'mensaje':'No se pudo crear el usuario'})
    else:
        formulario=UserRegistrationForm()
        return render(request, 'AppFinal/register.html', {'formulario':formulario})


#-------------------------Logout-------------------------


#----------------------------------------------------------

def editarPerfil(request):
    usuario=request.user

    if request.method == 'POST':
        formulario=UserEditForm(request.POST, instance=usuario)
        if formulario.is_valid():
            informacion=formulario.cleaned_data
            usuario.email=informacion['email']
            usuario.password1=informacion['password1']
            usuario.password2=informacion['password2']
            usuario.save()

            return render(request, 'AppFinal/inicio.html', {'usuario':usuario, 'mensaje':'PERFIL EDITADO EXITOSAMENTE'})
    else:
        formulario=UserEditForm(instance=usuario)
    return render(request, 'AppFinal/editarPerfil.html', {'formulario':formulario, 'usuario':usuario.username})

#---------------------------------------------------------------------------

def agregarAvatar(request):

    user=User.objects.get(username=request.user)
    if request.method == 'POST':
        formulario=AvatarForm(request.POST, request.FILES)
        if formulario.is_valid():

            avatarViejo=Avatar.objects.get(user=request.user)
            if(avatarViejo.avatar):
                avatarViejo.delete()

            avatar=Avatar(user=user, avatar=formulario.cleaned_data['avatar'])
            avatar.save()
            return render(request, 'AppFinal/inicio.html', {'usuario':user, 'mensaje':'AVATAR AGREGADO EXITOSAMENTE'})
    else:
        formulario=AvatarForm()
    return render(request, 'AppFinal/agregarAvatar.html', {'formulario':formulario, 'usuario':user})










