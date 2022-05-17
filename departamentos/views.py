from django.http import HttpResponse
from django.template import RequestContext
from django.shortcuts import render
from django.shortcuts import redirect
from django.utils import timezone
from departamentos.controllers.c_usuarios import registrar_usuario, iniciar_sesion, c_listar_usuarios, \
    c_deshabilitar_habilitar_usuario, registrar_usuario_rrhh
from departamentos.controllers.c_permisos import permisos_departamentos
from departamentos.controllers.c_nominas import datos_usuarios_nominas, asignar_nomina_usuario, \
    calcular_nominas_hasta_la_fecha, enviar_nominas_email
from departamentos.controllers.c_partes import c_ver_partes, anadir_partes, eliminar_parte
from departamentos.controllers.c_proyectos import anadir_proyecto, leer_proyectos
from departamentos.controllers.c_gastos import anadir_gasto, leer_gastos, eliminar_gasto
from departamentos.controllers.c_estadisticas import generar_graficos
from departamentos.controllers.c_objetivos import leer_objetivos, anadir_objetivo, eliminar_objetivo
from departamentos.controllers.c_valores import leer_valores, anadir_valor, eliminar_valor

# app basics
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


def estadisticas(request):
    estadisticas = generar_graficos()
    return render(request, 'estadisticas.html', {'estadisticas': estadisticas})


# dept rrhh
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
    return render(request, 'rrhh/asignar-nomina.html', {"datos": datos})


def alta_usuario(request):
    if request.method == 'POST':
        registrar_usuario_rrhh(request)
    return render(request, 'rrhh/alta-usuario.html')


# dept producción
def ver_partes(request):
    partes = c_ver_partes()
    return render(request, 'produccion/ver-partes.html', {'partes': partes})


def alta_proyecto(request):
    if request.method == 'POST':
        anadir_proyecto(request)
    proyectos = leer_proyectos()
    return render(request, 'produccion/alta-proyecto.html', {'proyectos': proyectos})


def alta_partes(request):
    if request.method == 'POST':
        anadir_partes(request)
    proyectos = leer_proyectos()
    return render(request, 'produccion/alta-parte.html', {'proyectos': proyectos})


def parte_delete(request):
    if request.method == 'POST':
        eliminar_parte(request)
    partes = c_ver_partes()
    return render(request, 'produccion/parte-delete.html', {'partes': partes})


# dept administración
def calculo_nominas(request):
    datos = calcular_nominas_hasta_la_fecha()
    return render(request, 'administracion/calculo-nominas.html', {'datos': datos})


def enviar_nominas(request):
    if request.method == 'POST':
        enviar_nominas_email()
        return redirect('/departamentos')
    datos = calcular_nominas_hasta_la_fecha()
    return render(request, 'administracion/enviar-nominas.html', {'datos': datos})


def crear_gasto(request):
    if request.method == 'POST':
        anadir_gasto(request)
    return render(request, 'administracion/crear-gasto.html')


def ver_gastos(request):
    return render(request, 'administracion/ver-gastos.html')


# dept comercial
def objetivos(request):
    if request.method == 'POST':
        if 'nombre' in request.POST:
            anadir_objetivo(request)
        else:
            eliminar_objetivo(request)
    objetivos = leer_objetivos()
    return render(request, 'comercial/objetivos.html', {'objetivos': objetivos})


def valores(request):
    if request.method == 'POST':
        if 'nombre' in request.POST:
            anadir_valor(request)
        else:
            eliminar_valor(request)
    valores = leer_valores()
    return render(request, 'comercial/valores.html', {'valores': valores})


def crear_eventos(request):
    return render(request, 'comercial/crear-eventos.html')


def ver_eventos(request):
    return render(request, 'comercial/ver-eventos.html')

