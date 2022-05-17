from departamentos.models import Objetivo


# obtener todos los objetivos
def leer_objetivos():
    return Objetivo.objects.all()


def anadir_objetivo(objetivo):
    objetivo.save()

def eliminar_objetivo(objetivo):
    objetivo.delete()
