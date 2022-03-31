import hashlib, json
from departamentos.modelos.permiso import Permiso
from departamentos.modelos.usuario import Usuario
from departamentos.controllers.c_permisos import leer_permisos, guardar_permisos
from departamentos.controllers.c_ficheros import leer_archivos, guardar_archivo


def proximo_usuario_id():
    usuarios = leer_archivos("usuarios.json")
    if len(usuarios) == 0:
        return 1
    else:
        return usuarios[-1]['id'] + 1

def c_listar_usuarios():
    return leer_usuarios()

def registrar_usuario(request):
    #Nuevo usuario
    id = proximo_usuario_id()
    nombre = request.POST['nombre']
    username = request.POST['user']
    password = hashlib.md5(request.POST['password'].encode('utf8')).hexdigest()
    email = request.POST['email']
    habilitado = True

    #Gestión de permisos
    permisos = leer_permisos()
    if "rrhh" in request.POST:
        permisos.append(Permiso(id, False, "1"))
    if "produccion" in request.POST:
        permisos.append(Permiso(id, False, "2"))
    if "administracion" in request.POST:
        permisos.append(Permiso(id, False, "3"))
    guardar_permisos(permisos)

    #crear el usuario
    usuario = Usuario(id, nombre, username, password, email, habilitado)

    #GUARDAR USUARIO
    #leer todos los usuarios
    usuarios = leer_usuarios()
    #poner el nuevo usuario en la lista
    usuarios.append(usuario)
    #guardarlos
    guardar_usuarios(usuarios)

def iniciar_sesion(request):
    usuarios = leer_usuarios()
    for usuario in usuarios:
        if usuario.username == request.POST['user'] and usuario.password == hashlib.md5(request.POST['password'].encode('utf8')).hexdigest() and usuario.habilitado:
            request.session['id_usuario'] = usuario.id
            return True
    return False

def leer_usuarios():
    usuariosJSON = leer_archivos("usuarios.json")
    usuarios = []
    for usuario in usuariosJSON:
        usuarios.append(Usuario.fromJSON(usuario))
    return usuarios

def guardar_usuarios(usuarios):
    usuariosJSON = []
    for usuario in usuarios:
        usuariosJSON.append(usuario.toJSON())
    guardar_archivo(usuariosJSON,"usuarios.json")

def c_deshabilitar_habilitar_usuario(id, habilitar):
    usuarios = leer_usuarios()
    for usuario in usuarios:
        if str(usuario.id) == str(id):
            if habilitar:
                #habilitar usuario
                usuario.habilitado = True
            else:
                #deshabilitar usuario
                usuario.habilitado = False
            break
    guardar_usuarios(usuarios)


def buscar_usuario_nombre_concreto(id):
    usuarios = leer_usuarios()
    for usuario in usuarios:
        if str(usuario.id) == str(id):
            return usuario.nombre
    return id


