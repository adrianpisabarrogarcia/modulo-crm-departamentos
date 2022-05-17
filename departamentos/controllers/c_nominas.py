import datetime
from django.core.mail import send_mail
from django.conf import settings
from departamentos.models import Usuario, Nomina


# obtener las nominas de un trabajador, si las tiene
def datos_usuarios_nominas():
    usuarios = Usuario.objects.all()
    datos_usuarios_nominas = []

    for usuario in usuarios:
        tiene_nomina = False
        nominas = Nomina.objects.filter(usuario=usuario)
        for nomina in nominas:
            if str(usuario.id) == str(nomina.usuario.id):
                usuario_nomina = {
                    "id": usuario.id,
                    "nombre": usuario.nombre,
                    "username": usuario.username,
                    "nomina": nomina.cantidad,
                    "fecha": nomina.fecha
                }
                datos_usuarios_nominas.append(usuario_nomina)
                tiene_nomina = True
        if not tiene_nomina:
            usuario_nomina = {
                "id": usuario.id,
                "nombre": usuario.nombre,
                "username": usuario.username
            }
            datos_usuarios_nominas.append(usuario_nomina)

    return datos_usuarios_nominas


# borrar la nomina anterior si la tiene y crear una nueva
def asignar_nomina_usuario(request):
    id_usuario = request.POST.get("id")
    cantidad = request.POST.get("nomina")
    # fecha de hoy
    now = datetime.datetime.now()
    fecha = now.strftime("%Y-%m-%d")

    # borrar la nomina anterior si la tiene
    usuario = Usuario.objects.get(id=int(id_usuario))
    nominas = Nomina.objects.filter(usuario=usuario)
    for nomina in nominas:
        nomina.delete()

    # crear una nueva nomina
    Nomina(usuario=usuario, cantidad=float(cantidad), fecha=fecha).save()


# obtener las nominas de un trabajador, si las tiene y las suma en función de la fecha
def calcular_nominas_hasta_la_fecha():
    nominas = Nomina.objects.all()

    datos_usuarios_nominas = []
    for nomina in nominas:
        nomina_base = nomina.cantidad
        fecha_nomina = nomina.fecha
        fecha_hoy = datetime.datetime.now()
        # meses entre las dos fechas
        meses = (fecha_hoy.year - fecha_nomina.year) * 12 + fecha_hoy.month - fecha_nomina.month
        nomina_mes = nomina_base / 12
        nomina_total = float(nomina_mes * meses)
        usuario_nomina = {
            "id": nomina.usuario.id,
            "nombre": nomina.usuario.nombre,
            "username": nomina.usuario.username,
            "email": nomina.usuario.email,
            "fecha": nomina.fecha,
            "meses": meses,
            "nomina_base": nomina_base,
            "nomina_total": nomina_total,
            "nomina_este_mes": nomina_mes,
        }
        datos_usuarios_nominas.append(usuario_nomina)

    return datos_usuarios_nominas


def enviar_nominas_email():
    nominas = calcular_nominas_hasta_la_fecha()
    for nomina in nominas:
        email = nomina["email"]
        nombre = nomina["nombre"]
        nomina_base = nomina["nomina_base"]
        nomina_total = nomina["nomina_total"]
        nomina_este_mes = nomina["nomina_este_mes"]
        fecha = nomina["fecha"]
        meses = nomina["meses"]
        email_message = "Hola " + nombre + ",\n\n"
        email_message += "Tu nomina base es de " + str(nomina_base) + "€.\n"
        email_message += "Tu nomina total es de " + str(nomina_total) + "€.\n"
        email_message += "Tu nomina este mes es de " + str(nomina_este_mes) + "€.\n"
        email_message += "\nMuchas gracias y esperemos que disfrutes del sueldo.\n"

        meses = ["enero", "febrero", "marzo", "abril", "mayo", "junio", "julio", "agosto", "septiembre", "octubre",
                 "noviembre", "diciembre"]
        mes_actual = meses[datetime.datetime.now().month - 1]
        # send mail
        send_mail(
            'Cálculo de nomina de ' + mes_actual + ' de ' + str(datetime.datetime.now().year),
            email_message,
            settings.EMAIL_HOST_USER,
            [email],
            fail_silently=False,
        )
