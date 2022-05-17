from django.db import models


# Models here.

class Departamento(models.Model):
    nombre = models.CharField(max_length=30)


class Gasto(models.Model):
    nombre = models.CharField(max_length=30)
    precio = models.FloatField()
    cantidad = models.IntegerField()
    fecha = models.DateField()


class Usuario(models.Model):
    nombre = models.CharField(max_length=30)
    username = models.CharField(max_length=30)
    password = models.CharField(max_length=60)
    email = models.EmailField()
    habilitado = models.BooleanField()


class Nomina(models.Model):
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    cantidad = models.FloatField()
    fecha = models.DateField()


class Proyecto(models.Model):
    nombre = models.CharField(max_length=30)


class Parte(models.Model):
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    proyecto = models.ForeignKey(Proyecto, on_delete=models.CASCADE)
    observacion = models.CharField(max_length=500)
    duracion = models.TimeField()
    fecha = models.DateField()


class Permiso(models.Model):
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    escritura = models.BooleanField()
    departamento = models.ForeignKey(Departamento, on_delete=models.CASCADE)


class Objetivo(models.Model):
    nombre = models.CharField(max_length=30)
    departamento = models.ForeignKey(Departamento, on_delete=models.CASCADE)
    descripcion = models.CharField(max_length=500)
    fechainicio = models.DateField()
    fechafin = models.DateField()

class Valores(models.Model):
    nombre = models.CharField(max_length=30)
    observacion = models.CharField(max_length=500)

class Evento(models.Model):
    nombre = models.CharField(max_length=30)
    fecha = models.DateField()
    hora = models.TimeField()
    lugar = models.CharField(max_length=30)
    descripcion = models.CharField(max_length=500)