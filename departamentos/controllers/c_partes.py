import csv
from django.http import HttpResponse
from departamentos.models import Parte, Usuario, Proyecto;


def c_ver_partes():
    partes = Parte.objects.all()
    return partes

def anadir_partes(request):
    #cojo el id del usuario de la sesión
    id_usuario = str(request.session.get('id_usuario'))
    proyecto = str(request.POST.get('proyecto'))
    observacion = str(request.POST.get('observacion'))
    duracion = str(request.POST.get('duracion'))
    fecha = str(request.POST.get('fecha'))

    parte = Parte(
        usuario=Usuario.objects.get(id=int(id_usuario)),
        proyecto=Proyecto.objects.get(id=int(proyecto)),
        observacion=observacion,
        duracion=duracion,
        fecha=fecha
    ).save()

def export_csv_partes():
    partes = Parte.objects.all()

    #genero el csv
    with open('partes.csv', 'w', newline='') as csvfile:
        fieldnames = ['id', 'id_usuario', 'nombre_usuario', 'id_proyecto', 'nombre_proyecto', 'observacion', 'duracion', 'fecha']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        for parte in partes:
            writer.writerow({'id': str(parte.id), 'id_usuario': str(parte.usuario.id), 'nombre_usuario': parte.usuario.nombre, 'id_proyecto': str(parte.proyecto.id), 'nombre_proyecto': parte.proyecto.nombre, 'observacion': parte.observacion, 'duracion': str(parte.duracion), 'fecha': str(parte.fecha)})

        #return a response
        response = HttpResponse(content_type='text/csv')
        response['Content-Disposition'] = 'attachment; filename="partes.csv"'
        return response

def eliminar_parte(request):
    id = str(request.POST.get('id'))
    Parte.objects.filter(id=int(id)).delete()