from departamentos.models import Evento


# obtener todos los objetivos
def leer_eventos():
    return Evento.objects.all()


def anadir_evento(request):
    evento = Evento()
    evento.nombre = request.POST['nombre']
    evento.descripcion = request.POST['descripcion']
    evento.fecha = request.POST['fecha']
    evento.hora = request.POST['hora']
    evento.lugar = request.POST['lugar']
    evento.save()
    return evento


def eliminar_evento(request):
    evento = Evento.objects.get(id=request.POST['id'])
    evento.delete()



