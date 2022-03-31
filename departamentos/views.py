from django.http import HttpResponse
from django.template import RequestContext
from django.shortcuts import render
from django.shortcuts import redirect
from django.utils import timezone
from departamentos.controllers.c_usuarios import registrar_usuario, iniciar_sesion, c_listar_usuarios, c_deshabilitar_habilitar_usuario
from departamentos.controllers.c_permisos import permisos_departamentos
from departamentos.controllers.c_nominas import datos_usuarios_nominas, asignar_nomina_usuario
from departamentos.controllers.c_partes import c_ver_partes

#app basics
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


#dept rrhh
def listar_usuarios(request):
    usuarios = c_listar_usuarios()
    return render(request, 'rrhh/lista-usuarios.html', {'usuarios': usuarios})

def habilitar_deshabilitar_usuario(request):
    usuarios = c_listar_usuarios()
    return render(request, 'rrhh/habilitar-deshabilitar.html', {'usuarios': usuarios})

def deshabilitar_usuario(request):
    id_usuario = request.GET.get('id')
    c_deshabilitar_habilitar_usuario(id_usuario, False)
    return redirect('/rrhh/habilitar-deshabilitar')

def habilitar_usuario(request):
    id_usuario = request.GET.get('id')
    c_deshabilitar_habilitar_usuario(id_usuario, True)
    return redirect('/rrhh/habilitar-deshabilitar')

def asignar_nomina(request):
    if request.method == 'POST':
        asignar_nomina_usuario(request)
    datos = datos_usuarios_nominas()
    #return render(request, 'rrhh/asignar-nomina.html', {usuarios_nominas: usuarios_nominas})
    return render(request, 'rrhh/asignar-nomina.html', {"datos" : datos })

#dept producción
def ver_partes(request):
    partes = c_ver_partes()
    return render(request, 'produccion/ver-partes.html', {'partes': partes})