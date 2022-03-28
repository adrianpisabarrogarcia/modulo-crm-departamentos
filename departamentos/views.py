from django.http import HttpResponse
from django.template import RequestContext
from django.shortcuts import render
from django.shortcuts import redirect
from django.utils import timezone
from departamentos.controllers.c_usuarios import registrar_usuario, iniciar_sesion

#para iniciar sesion mediante post y get para el formulario
def index(request):
    if request.method == 'POST':
        if iniciar_sesion(request):
            return redirect('/departamentos')
        else:
            return render(request, 'sign-in.html', {'error': 'Usuario o contraseña incorrectos'})
    return render(request, 'sign-in.html')


def register(request):
    if request.method == 'POST':
        registrar_usuario(request)
        return redirect('/')
    return render(request, 'register.html')


def departamentos(request):
    return render(request, 'departamentos.html')
