from departamentos.models import Permiso, Usuario

def permisos_departamentos(id_usuario):
    permisos = Permiso.objects.filter(user=Usuario.objects.get(id=int(id_usuario)))
    permisos_departamentos = []
    for permiso in permisos:
        if str(permiso.id_usuario) == str(id_usuario):
            # guardo el id del departamento para saber que departamento tiene permiso ese usuario y si tiene permiso para escribir o ver
            permisos_departamentos.append({
                "departamento": str(permiso.id_departamento),
                "escritura": permiso.escritura,
            })
    return permisos_departamentos
