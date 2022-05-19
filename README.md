# Módulo ERP para gestión de Departamentos

## Tecnologías
Este repositorio sirve para el aprendizaje de:   

* Python
* Django
* BBDD (Django Models, SQLLite)
* MVC (Model View Controller)

## Documentación
El documento con el Manual de Usuario, se encuentra en este enlace: [https://labur.eus/zqjEl](https://labur.eus/zqjEl)


## Cómo iniciar el proyecto con Django
1. Descargar el repo
2. Instalar Django con `pip install django`
3. Ejecutar el comando `python3 manage.py migrate`
4. Ejecutar el comando `python3 manage.py makemigrations`
5. Ejecutar el servidor embebido `python3 manage.py runserver`

## Otra documentación del Framework

### Comandos para Migrations con SQL Lite
1. Escribir las classes en el archivo `models.py`
2. Ejecutar el comando `python3 manage.py makemigrations`
3. Ejecutar el comando `python3 manage.py migrate`
4. Ejecutar el comando `python3 manage.py runserver`

#### SELECT
```python
usuarios = Usuario.objects.filter(username=request.POST['user'])
```
#### INSERT
```python
usuario = Usuario(nombre=nombre, username=username, password=password, email=email, habilitado=habilitado)
usuario.save()
```
#### UPDATE
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

#### DELETE
```python
usuario = Usuario.objects.get(id=int(id))
usuario.delete()
```