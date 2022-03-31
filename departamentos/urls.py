
from django.urls import path
from departamentos import views



urlpatterns = [
    path('', views.index, name='index'),
    path("register/", views.register, name="register"),
    path("departamentos/", views.departamentos, name="departamentos"),
    path("sign-out/", views.cerrar_sesion, name="cerrar_sesion"),
    path("rrhh/lista-usuarios/", views.listar_usuarios, name="listar_usuarios"),
    path("rrhh/deshabilitar", views.deshabilitar_usuario, name="deshabilitar_usuario"),
    path("rrhh/habilitar", views.habilitar_usuario, name="habilitar_usuario"),
    path("rrhh/habilitar-deshabilitar", views.habilitar_deshabilitar_usuario, name="habilitar_deshabilitar_usuario"),
    path("rrhh/asignar-nomina", views.asignar_nomina, name="asignar_nomina"),
    path("produccion/ver-partes", views.ver_partes, name="ver_partes"),
    path("produccion/alta-proyecto", views.alta_proyecto, name="alta_proyecto"),
    path("produccion/alta-parte", views.alta_partes, name="alta_partes"),
    path("produccion/parte-delete", views.parte_delete, name="parte_delete"),
]