from departamentos.models import Valores


# obtener todos los objetivos
def leer_valores():
    return Valores.objects.all()


def anadir_valor(request):
    valores = Valores()
    valores.nombre = request.POST['nombre']
    valores.observacion = request.POST['observacion']
    valores.save()


def eliminar_valor(request):
    valor = Valores.objects.get(id=int(request.POST['id']))
    valor.delete()

