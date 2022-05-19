from django.urls import path
from AppFinal import views
from .views import *

urlpatterns = [   
    path('',inicio, name='inicio'), 
    path('usuario/',usuario, name='usuario'),
    path('animal/',animal, name='animal'),
    path('datos/',datos, name='datos'),
    path('buscarUsuario/', buscarUsuario, name='buscarUsuario')

]