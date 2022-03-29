from departamentos.controllers.c_ficheros import leer_archivos, guardar_archivo
from departamentos.modelos.parte import Parte


def leer_partes():
    partesJSON = leer_archivos("permisos.json")
    partes = []
    for parte in partesJSON:
        partes.append(Parte.fromJSON(parte))
    return partes

def guardar_partes(partes):
    partesJSON = []
    for parte in partes:
        partesJSON.append(parte.toJSON())
    guardar_archivo(partesJSON, "partes.json")

