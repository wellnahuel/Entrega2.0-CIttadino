from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Usuario(models.Model):
    nombre= models.CharField(max_length=30)
    apellido= models.CharField(max_length=30)
    email= models.EmailField(max_length=40)
    celular= models.IntegerField()

    def __str__(self):
        return self.nombre+ " " + self.apellido + " " + self.email + " " + str(self.celular)

class Animal(models.Model):
    raza= models.CharField(max_length=30)
    color= models.CharField(max_length=30)

    def __str__(self):
        return self.raza+ " " + self.color + " "
   
class Datos(models.Model):
    fecha = models.DateField()  
    lugar= models.CharField(max_length=30)
    condicion= models.CharField(max_length=30)

    def __str__(self):
        return str(self.fecha)+ " " + self.lugar + " " + self.condicion 

class Avatar(models.Model):
    user=models.ForeignKey(User, on_delete=models.CASCADE)
    avatar= models.ImageField(upload_to='avatar', blank=True, null=True)