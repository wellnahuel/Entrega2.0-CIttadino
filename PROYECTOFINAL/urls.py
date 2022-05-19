from django.contrib import admin
from django.urls import path, include
from AppFinal.views import *


urlpatterns = [
    path('admin/', admin.site.urls),
    path('AppFinal/', include('AppFinal.urls')),
]
