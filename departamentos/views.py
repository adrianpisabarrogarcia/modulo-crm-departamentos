from django.http import HttpResponse
from django.template import RequestContext
from django.shortcuts import render
from django.shortcuts import redirect
from django.utils import timezone
from departamentos.controllers.c_usuarios import registrar_usuario, iniciar_sesion, c_listar_usuarios
from departamentos.controllers.c_permisos import permisos_departamentos

#para iniciar sesion mediante post y get para el formulario
def index(request):
    if request.method == 'POST':
        if iniciar_sesion(request):
            return redirect('/departamentos')
        else:
            return render(request, 'sign-in.html', {'error': True})
    return render(request, 'sign-in.html')


def register(request):
    if request.method == 'POST':
        registrar_usuario(request)
        return redirect('/')
    return render(request, 'register.html')


def departamentos(request):
    if request.session.get('id_usuario'):
        permisos = permisos_departamentos(request.session.get('id_usuario'))
        return render(request, 'departamentos.html', {'permisos': permisos})
    return redirect('/')

def cerrar_sesion(request):
    request.session.flush()
    return redirect('/')



def listar_usuarios(request):
    usuarios = c_listar_usuarios()
    return render(request, 'rrhh/lista-usuarios.html', {'usuarios': usuarios})

