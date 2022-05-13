from departamentos.models import Proyecto

def buscar_proyecto_nombre_concreto(id_proyecto):
    return Proyecto.objects.get(id=id_proyecto).nombre

def anadir_proyecto(request):
    nombre = request.POST.get("nombre")
    Proyecto(nombre=nombre).save()