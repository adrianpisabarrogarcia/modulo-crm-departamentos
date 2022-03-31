from django.http import HttpResponse

from departamentos.controllers.c_ficheros import leer_archivos, guardar_archivo
from departamentos.controllers.c_usuarios import buscar_usuario_nombre_concreto;
from departamentos.controllers.c_proyectos import buscar_proyecto_nombre_concreto;

from departamentos.modelos.parte import Parte


def leer_partes():
    partesJSON = leer_archivos("partes.json")
    partes = []
    for parte in partesJSON:
        partes.append(Parte.fromJSON(parte))
    return partes

def guardar_partes(partes):
    partesJSON = []
    for parte in partes:
        partesJSON.append(parte.toJSON())
    guardar_archivo(partesJSON, "partes.json")

def c_ver_partes():
    partes = leer_partes()
    for parte in partes:
        parte.id_usuario = str(buscar_usuario_nombre_concreto(parte.id_usuario))
        parte.proyecto = str(buscar_proyecto_nombre_concreto(parte.proyecto))
    return partes

def proximo_id_parte():
    partes = leer_partes()
    if len(partes) == 0:
        return 1
    else:
        return partes[-1].id + 1

def anadir_partes(request):
    id = proximo_id_parte()
    #cojo el id del usuario de la sesión
    id_usuario = str(request.session.get('id_usuario'))
    proyecto = str(request.POST.get('proyecto'))
    observacion = str(request.POST.get('observacion'))
    duracion = str(request.POST.get('duracion'))
    fecha = str(request.POST.get('fecha'))

    parte = Parte(id, id_usuario, proyecto, observacion, duracion, fecha)
    partes = leer_partes()
    partes.append(parte)
    guardar_partes(partes)

def export_csv_partes():
    partes = leer_partes()
    for parte in partes:
        parte.id_usuario = str(buscar_usuario_nombre_concreto(parte.id_usuario))
        parte.proyecto = str(buscar_proyecto_nombre_concreto(parte.proyecto))

    #genero el csv
    with open('partes.csv', 'w', newline='') as csvfile:
        fieldnames = ['id', 'id_usuario', 'proyecto', 'observacion', 'duracion', 'fecha']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        for parte in partes:
            writer.writerow({'id': parte.id, 'id_usuario': parte.id_usuario, 'proyecto': parte.proyecto, 'observacion': parte.observacion, 'duracion': parte.duracion, 'fecha': parte.fecha})

        #return a response
        response = HttpResponse(content_type='text/csv')
        response['Content-Disposition'] = 'attachment; filename="partes.csv"'
        return response


def eliminar_parte(request):
    id = str(request.POST.get('id'))
    partes = leer_partes()
    for parte in partes:
        if str(parte.id) == str(id):
            partes.remove(parte)
            break
    guardar_partes(partes)