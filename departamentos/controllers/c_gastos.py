from departamentos.controllers.c_ficheros import leer_archivos, guardar_archivo
from departamentos.modelos.gasto import Gasto



def leer_gastos():
    gastosJSON = leer_archivos("gastos.json")
    gastos = []
    for gasto in gastosJSON:
        gastos.append(Gasto.fromJSON(gasto))
    return gastos

def guardar_gastos(gastos):
    gastosJSON = []
    for gasto in gastos:
        gastosJSON.append(gasto.toJSON())
    guardar_archivo(gastosJSON, "gastos.json")

def proximo_id_gastos():
    gastos = leer_gastos()
    if len(gastos) == 0:
        return 1
    else:
        return gastos[-1].id + 1

def anadir_gasto(request):
    gastos = leer_gastos()
    id = proximo_id_gastos()
    nombre = request.POST["nombre"]
    precio = request.POST["precio"]
    cantidad = request.POST["cantidad"]
    fecha = request.POST["fecha"]
    gasto = Gasto(id, nombre, precio, cantidad, fecha)
    gastos.append(gasto)
    guardar_gastos(gastos)

def eliminar_gasto(request):
    gastos = leer_gastos()
    id = request.POST["id"]
    for gasto in gastos:
        if str(gasto.id) == str(id):
            gastos.remove(gasto)
            break
    guardar_gastos(gastos)