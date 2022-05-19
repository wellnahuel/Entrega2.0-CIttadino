from django.contrib import admin

from .models import Datos, Usuario, Animal

# Register your models here.
admin.site.register(Usuario)
admin.site.register(Datos)
admin.site.register(Animal)