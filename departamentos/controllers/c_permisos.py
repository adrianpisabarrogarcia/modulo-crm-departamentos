from ..models.permiso import Permiso

def proximo_permiso_id():
    permisos = leer_archivos("permisos.json")
    if len(permisos) == 0:
        return 1
    else:
        return permisos[-1]['id'] + 1
