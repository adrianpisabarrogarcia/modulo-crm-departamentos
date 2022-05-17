from departamentos.models import Objetivo, Departamento


# obtener todos los objetivos
def leer_objetivos():
    return Objetivo.objects.all()


def anadir_objetivo(request):
    objetivo = Objetivo()
    objetivo.nombre = request.POST['nombre']
    objetivo.descripcion = request.POST['descripcion']
    objetivo.departamento = Departamento.objects.get(id=int(request.POST['departamento']))
    objetivo.fechainicio = request.POST['fecha-inicio']
    objetivo.fechafin = request.POST['fecha-fin']
    objetivo.save()

def eliminar_objetivo(request):
    objetivo = Objetivo.objects.get(id=int(request.POST['id']))
    objetivo.delete()
