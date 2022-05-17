from departamentos.models import Gasto


def leer_gastos():
    gastos = Gasto.objects.all()

    gastos_personalizados = []
    for gasto in gastos:
        gastos_personalizados.append(
            {
                "id": gasto.id,
                "nombre": gasto.nombre,
                "precio": gasto.precio,
                "cantidad": gasto.cantidad,
                "total": float(gasto.precio * gasto.cantidad),
                "fecha": gasto.fecha
            }
        )
    return gastos_personalizados


def anadir_gasto(request):
    nombre = request.POST["nombre"]
    precio = request.POST["precio"]
    cantidad = request.POST["cantidad"]
    fecha = request.POST["fecha"]
    Gasto(nombre=nombre, precio=float(precio), cantidad=int(cantidad), fecha=fecha).save()


def eliminar_gasto(request):
    id = request.POST["id"]
    Gasto.objects.get(id=int(id)).delete()
