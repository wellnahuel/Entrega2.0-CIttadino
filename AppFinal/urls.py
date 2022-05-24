from django.urls import path
from AppFinal import views
from .views import *
from django.contrib.auth.views import LogoutView

urlpatterns = [   
    path('',inicio, name='inicio'), 
    path('usuario/',usuario, name='usuario'),
    path('animal/',animal, name='animal'),
    path('datos/',datos, name='datos'),
    path('buscarUsuario/', buscarUsuario, name='buscarUsuario'),
    path('leerUsuarios', views.leerUsuarios, name='LeerUsuarios'),
    path('eliminarUsuario/<nombre>', eliminarUsuario, name='eliminarUsuario'),
    path('editarUsuario/<nombre>', editarUsuario, name='editarUsuario'),

    #-------------------------------------

    path('animal/list/', AnimalesList.as_view(), name='animal_listar'),
    path('animal/<pk>', AnimalDetalle.as_view(), name='animal_detalle'),
    path('animal/nuevo/', AnimalCreacion.as_view(), name='animal_crear'),
    path('animal/editar/<pk>', AnimalEdicion.as_view(),name='animal_editar'),
    path('animal/borrar/<pk>', AnimalEliminacion.as_view(), name='animal_borrar'),

    path('login', login_request, name='login'),
    path('register', register, name='register'),

    path('logout', LogoutView.as_view(template_name='AppFinal/logout.html'), name='logout'),

    path('editarPerfil', editarPerfil, name='editarPerfil'),
    path('agregarAvatar', agregarAvatar, name='agregarAvatar'),

]