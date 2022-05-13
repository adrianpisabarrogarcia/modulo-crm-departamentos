# Módulo ERP para gestión de Departamentos

Este repositorio sirve para el aprendizaje de:   

* Python
* Archivos (logs, json)
* Django

El documento con el Manual de Usuario, se encuentra en este enlace: [https://labur.eus/EGZNf](https://docs.google.com/document/d/1-QjsB7f2ocSsPC19IoQjOdb2CFdaheEljGYwRvXf78s/edit?usp=sharing)

## Comandos para Migrations con SQL Lite
1. Escribir las classes en el archivo `models.py`
2. Ejecutar el comando `python3 manage.py makemigrations`
3. Ejecutar el comando `python3 manage.py migrate`
4. Ejecutar el comando `python3 manage.py runserver`

## Pasar a SQL   
 - [] Eliminar ficheros
 - [] Gastos
 - [] Nominas
 - [] Partes
 - [✅] Permisos
 - [] Proyectos
 - [✅] Usuarios
### SELECT
```python
usuarios = Usuario.objects.filter(username=request.POST['user'])
```
### INSERT
```python
usuario = Usuario(nombre=nombre, username=username, password=password, email=email, habilitado=habilitado)
usuario.save()
```
### UPDATE
```python
usuario = Usuario.objects.get(id=int(id))
if habilitar:
    # habilitar usuario
    usuario.habilitado = True
else:
    # deshabilitar usuario
    usuario.habilitado = False
usuario.save()
```

### UPDATE
```python
usuario = Usuario.objects.get(id=int(id))
usuario.delete()
```