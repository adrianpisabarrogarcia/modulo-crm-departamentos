import datetime

from departamentos.controllers.c_usuarios import leer_usuarios
from departamentos.controllers.c_ficheros import guardar_archivo, leer_archivos
from departamentos.modelos.nomina import Nomina


def leer_nominas():
    nominasJSON = leer_archivos("nominas.json")
    nominas = []
    for nomina in nominasJSON:
        nominas.append(Nomina.fromJSON(nomina))
    return nominas

def guardar_nominas(nominas):
    nominasJSON = []
    for nomina in nominas:
        nominasJSON.append(nomina.toJSON())
    guardar_archivo(nominasJSON, "nominas.json")

# obtener las nominas de un trabajador, si las tiene
def datos_usuarios_nominas():
    usuarios = leer_usuarios()
    nominas = leer_nominas()

    datos_usuarios_nominas = []

    for usuario in usuarios:
        tiene_nomina = False
        for nomina in nominas:
            if str(usuario.id) == str(nomina.id_usuario):
                usuario_nomina = {
                    "id": usuario.id,
                    "nombre": usuario.nombre,
                    "username": usuario.username,
                    "nomina": nomina.cantidad,
                    "fecha": nomina.fecha
                }
                datos_usuarios_nominas.append(usuario_nomina)
                tiene_nomina = True
        if not tiene_nomina:
            usuario_nomina = {
                "id": usuario.id,
                "nombre": usuario.nombre,
                "username": usuario.username
            }
            datos_usuarios_nominas.append(usuario_nomina)

    return datos_usuarios_nominas

# borrar la nomina anterior si la tiene y crear una nueva
def asignar_nomina_usuario(request):
    nominas = leer_nominas()
    usuarios = leer_usuarios()
    id_usuario = request.POST.get("id")
    cantidad = request.POST.get("nomina")
    # fecha de hoy
    now = datetime.datetime.now()
    fecha = now.strftime("%Y-%m-%d")
    for nomina in nominas:
        if str(nomina.id_usuario) == str(id_usuario):
            nominas.remove(nomina)
    nomina = Nomina(str(id_usuario), str(cantidad), str(fecha))
    nominas.append(nomina)
    guardar_nominas(nominas)

# obtener las nominas de un trabajador, si las tiene y las suma en función de la fecha
def calcular_nominas_hasta_la_fecha():
    nominas = leer_nominas()

    for nomina in nominas:
        fecha_nomina = datetime.datetime.strptime(nomina.fecha, "%Y-%m-%d")
        fecha_hoy = datetime.datetime.now()
        #meses entre las dos fechas
        meses = (fecha_hoy.year - fecha_nomina.year) * 12 + fecha_hoy.month - fecha_nomina.month
        nomina.cantidad = float(nomina.cantidad) * meses

    usuarios = leer_usuarios()
    datos_usuarios_nominas = []
    for usuario in usuarios:
        for nomina in nominas:
            if str(usuario.id) == str(nomina.id_usuario):
                nomina_base = nomina.cantidad
                fecha_nomina = datetime.datetime.strptime(nomina.fecha, "%Y-%m-%d")
                fecha_hoy = datetime.datetime.now()
                #meses entre las dos fechas
                meses = (fecha_hoy.year - fecha_nomina.year) * 12 + fecha_hoy.month - fecha_nomina.month
                nomina_total = float(nomina_base) * meses
                nomina_mes = nomina_base / 12
                usuario_nomina = {
                    "id": usuario.id,
                    "nombre": usuario.nombre,
                    "username": usuario.username,
                    "email": usuario.email,
                    "fecha": nomina.fecha,
                    "meses": meses,
                    "nomina_base": nomina_base,
                    "nomina_total": nomina_total,
                    "nomina_este_mes": nomina_base,
                }
                datos_usuarios_nominas.append(usuario_nomina)
    return datos_usuarios_nominas



