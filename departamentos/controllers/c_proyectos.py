from departamentos.controllers.c_ficheros import leer_archivos, guardar_archivo
from departamentos.modelos.proyecto import Proyecto



def leer_proyectos():
    proyectosJSON = leer_archivos("usuarios.json")
    proyectos = []
    for proyecto in proyectosJSON:
        proyectos.append(Proyecto.fromJSON(proyecto))
    return proyectos

def guardar_usuarios(proyectos):
    proyectosJSON = []
    for proyecto in proyectos:
        proyectosJSON.append(proyecto.toJSON())
    guardar_archivo(proyectosJSON,"proyectos.json")


def buscar_proyecto_nombre_concreto(id_proyecto):
    proyectos = leer_proyectos()
    for proyecto in proyectos:
        if proyecto.id_proyecto == id_proyecto:
            return proyecto.nombre
    return id_proyecto