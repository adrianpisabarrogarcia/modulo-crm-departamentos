import hashlib
from ..models.departamento import Departamento
from ..models.permiso import Permiso
from ..models.usuario import Usuario
from c_permisos import proximo_permiso_id

from c_ficheros import leer_archivos, guardar_archivo


def proximo_usuario_id():
    usuarios = leer_archivos("usuarios.json")
    if len(usuarios) == 0:
        return 1
    else:
        return usuarios[-1]['id'] + 1


def listar_usuarios(request):
    usuarios = leer_archivos("usuarios.json")
    print(usuarios)
    return usuarios

def registrar_usuario(request):
    usuario = Usuario()
    usuario.id = proximo_usuario_id()
    usuario.nombre = request.POST['nombre']
    usuario.username = request.POST['username']
    usuario.password = hashlib.md5(request.POST['password'].encode('utf8')).hexdigest()
    usuario.email = request.POST['email']
    usuario.habilitado = True
    usuario.nomina = None
    if "rrhh" in request.POST:
        usuario.permisos.append(
            #false para permisos de solo lectura
            Permiso(proximo_permiso_id(), False,
                    Departamento("1", "RRHH"))
        )
    if "produccion" in request.POST:
        usuario.permisos.append(
            #false para permisos de solo lectura
            Permiso(proximo_permiso_id(), False,
                    Departamento("2", "Producción"))
        )
    if "administracion" in request.POST:
        usuario.permisos.append(
            #false para permisos de solo lectura
            Permiso(proximo_permiso_id(), False,
                    Departamento("3", "Administración"))
        )

    #abrir todos los usuarios
    usuarios = leer_archivos("usuarios.json")
    #agregar el nuevo usuario
    usuarios.append(usuario.to_json())
    #guardar usuarios en archivo json
    guardar_archivo("usuarios.json", usuarios)
