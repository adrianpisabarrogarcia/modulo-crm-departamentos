from departamentos.models import Gasto


def anadir_gasto(request):
    nombre = request.POST["nombre"]
    precio = request.POST["precio"]
    cantidad = request.POST["cantidad"]
    fecha = request.POST["fecha"]
    Gasto(nombre=nombre, precio=float(precio), cantidad=int(cantidad), fecha=fecha).save()

def eliminar_gasto(request):
    id = request.POST["id"]
    Gasto.objects.get(id=int(id)).delete()