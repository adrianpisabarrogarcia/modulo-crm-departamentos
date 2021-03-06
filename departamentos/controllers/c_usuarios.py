import hashlib
from departamentos.models import Usuario, Permiso, Departamento


def c_listar_usuarios():
    return Usuario.objects.all()

def registrar_usuario(request):
    # Nuevo usuario
    nombre = request.POST['nombre']
    username = request.POST['user']
    password = hashlib.md5(request.POST['password'].encode('utf8')).hexdigest()
    email = request.POST['email']
    habilitado = True

    # Crear usuario
    usuario = Usuario(nombre=nombre, username=username, password=password, email=email, habilitado=habilitado)
    usuario.save()

    # Gestión de permisos del usuario
    if "rrhh" in request.POST:
        Permiso(usuario=usuario, escritura=False, departamento=Departamento.objects.get(id=1)).save()
    if "produccion" in request.POST:
        Permiso(usuario=usuario, escritura=False, departamento=Departamento.objects.get(id=2)).save()
    if "administracion" in request.POST:
        Permiso(usuario=usuario, escritura=False, departamento=Departamento.objects.get(id=3)).save()
    if "comercial" in request.POST:
        Permiso(usuario=usuario, escritura=False, departamento=Departamento.objects.get(id=4)).save()


def iniciar_sesion(request):
    usuarios = Usuario.objects.filter(username=request.POST['user'])

    for usuario in usuarios:
        if usuario.username == request.POST['user'] and usuario.password == hashlib.md5(
                request.POST['password'].encode('utf8')).hexdigest() and usuario.habilitado:
            request.session['id_usuario'] = usuario.id
            return True
    return False


def c_deshabilitar_habilitar_usuario(id, habilitar):
    usuario = Usuario.objects.get(id=int(id))
    if habilitar:
        # habilitar usuario
        usuario.habilitado = True
    else:
        # deshabilitar usuario
        usuario.habilitado = False
    usuario.save()

def registrar_usuario_rrhh(request):
    # Nuevo usuario
    nombre = request.POST['nombre']
    username = request.POST['usuario']
    password = hashlib.md5(request.POST['password'].encode('utf8')).hexdigest()
    email = request.POST['email']
    habilitado = True

    # crear el usuario
    usuario = Usuario(nombre=nombre, username=username, password=password, email=email, habilitado=habilitado)
    usuario.save()

    # Gestión de permisos
    if "rrhh" in request.POST:
        if request.POST['rrhh-checkbox'] == "lectura":
            Permiso(usuario=usuario, escritura=False, departamento=Departamento.objects.get(id=1)).save()
        else:
            Permiso(usuario=usuario, escritura=True, departamento=Departamento.objects.get(id=1)).save()
    if "produccion" in request.POST:
        if request.POST['produccion-checkbox'] == "lectura":
            Permiso(usuario=usuario, escritura=False, departamento=Departamento.objects.get(id=2)).save()
        else:
            Permiso(usuario=usuario, escritura=True, departamento=Departamento.objects.get(id=2)).save()
    if "administracion" in request.POST:
        if request.POST['administracion-checkbox'] == "lectura":
            Permiso(usuario=usuario, escritura=False, departamento=Departamento.objects.get(id=3)).save()
        else:
            Permiso(usuario=usuario, escritura=True, departamento=Departamento.objects.get(id=3)).save()
    if "comercial" in request.POST:
        if request.POST['comercial-checkbox'] == "lectura":
            Permiso(usuario=usuario, escritura=False, departamento=Departamento.objects.get(id=4)).save()
        else:
            Permiso(usuario=usuario, escritura=True, departamento=Departamento.objects.get(id=4)).save()