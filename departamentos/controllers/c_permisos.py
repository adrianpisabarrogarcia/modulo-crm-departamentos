from departamentos.controllers.c_ficheros import leer_archivos, guardar_archivo
from departamentos.modelos.permiso import Permiso



def leer_permisos():
    permisosJSON = leer_archivos("permisos.json")
    print(permisosJSON)
    permisos = []
    for permiso in permisosJSON:
        permisos.append(Permiso.fromJSON(permiso))
    return permisos

def guardar_permisos(permisos):
    permisosJSON = []
    for permiso in permisos:
        permisosJSON.append(permiso.toJSON())
    guardar_archivo(permisosJSON,"permisos.json")