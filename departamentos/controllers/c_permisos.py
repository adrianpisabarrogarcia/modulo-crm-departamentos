from departamentos.controllers.c_ficheros import leer_archivos, guardar_archivo
from departamentos.modelos.permiso import Permiso


def leer_permisos():
    permisosJSON = leer_archivos("permisos.json")
    permisos = []
    for permiso in permisosJSON:
        permisos.append(Permiso.fromJSON(permiso))
    return permisos

def guardar_permisos(permisos):
    permisosJSON = []
    for permiso in permisos:
        permisosJSON.append(permiso.toJSON())
    guardar_archivo(permisosJSON, "permisos.json")

def permisos_departamentos(id_usuario):
    permisos = leer_permisos()
    permisos_departamentos = []
    for permiso in permisos:
        if str(permiso.id_usuario) == str(id_usuario):
            # guardo el id del departamento para saber que departamento tiene permiso ese usuario y si tiene permiso para escribir o ver
            permisos_departamentos.append({
                "departamento": str(permiso.id_departamento),
                "escritura": permiso.escritura,
            })
    return permisos_departamentos
