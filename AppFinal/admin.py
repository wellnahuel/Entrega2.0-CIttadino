from django.contrib import admin

from .models import Datos, Usuario, Animal, Avatar

# Register your models here.
admin.site.register(Usuario)
admin.site.register(Datos)
admin.site.register(Animal)
admin.site.register(Avatar)