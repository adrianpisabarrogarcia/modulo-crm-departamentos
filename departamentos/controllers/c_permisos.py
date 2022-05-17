from departamentos.models import Permiso, Usuario

def permisos_departamentos(id_usuario):
    permisos = Permiso.objects.filter(usuario=Usuario.objects.get(id=int(id_usuario)))
    permisos_departamentos = []
    for permiso in permisos:
        if int(permiso.usuario.id) == int(id_usuario):
            # guardo el id del departamento para saber que departamento tiene permiso ese usuario y si tiene permiso para escribir o ver
            permisos_departamentos.append({
                "departamento": str(permiso.departamento.id),
                "escritura": permiso.escritura,
            })
    return permisos_departamentos
