
from django.urls import path
from departamentos import views



urlpatterns = [
    path('', views.index, name='index'),
    path("register/", views.register, name="register"),
    path("departamentos/", views.departamentos, name="departamentos"),
    path("sign-out/", views.cerrar_sesion, name="cerrar_sesion"),
    path("rrhh/lista-usuarios/", views.listar_usuarios, name="listar_usuarios"),
]