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

#obtener las nominas de un trabajador, si las tiene
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
                    "nomina" : nomina.cantidad,
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

#borrar la nomina anterior si la tiene y crear una nueva
def asignar_nomina_usuario(request):
    nominas = leer_nominas()
    usuarios = leer_usuarios()
    id_usuario = request.POST.get("id")
    cantidad = request.POST.get("nomina")
    #fecha de hoy
    now = datetime.datetime.now()
    fecha = now.strftime("%Y-%m-%d")
    for nomina in nominas:
        if str(nomina.id_usuario) == str(id_usuario):
            nominas.remove(nomina)
    nomina = Nomina(str(id_usuario), str(cantidad), str(fecha))
    nominas.append(nomina)
    guardar_nominas(nominas)
