from departamentos.controllers.c_ficheros import leer_archivos, guardar_archivo
from departamentos.controllers.c_usuarios import buscar_usuario_nombre_concreto;
from departamentos.controllers.c_proyectos import buscar_proyecto_nombre_concreto;

from departamentos.modelos.parte import Parte


def leer_partes():
    partesJSON = leer_archivos("partes.json")
    partes = []
    for parte in partesJSON:
        partes.append(Parte.fromJSON(parte))
    return partes

def guardar_partes(partes):
    partesJSON = []
    for parte in partes:
        partesJSON.append(parte.toJSON())
    guardar_archivo(partesJSON, "partes.json")

def c_ver_partes():
    partes = leer_partes()
    for parte in partes:
        parte.id_usuario = str(buscar_usuario_nombre_concreto(parte.id_usuario))
        parte.proyecto = str(buscar_proyecto_nombre_concreto(parte.proyecto))
    return partes