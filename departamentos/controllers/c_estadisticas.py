import datetime
import os
import matplotlib
import matplotlib.pyplot as plt
matplotlib.use('Agg')

import numpy as np
import pathlib
from departamentos.models import Nomina, Parte, Proyecto



def generar_graficos():
    return {
        "sueldos": ranking_sueldos(),
        "partes": cuantos_partes_por_cada_proyecto(),
    }

# guardar el gráfico y devolver la ruta en la que esta guardado
def generar_archivo():
    nombre_fichero = str(datetime.datetime.now()).replace(':', '-').replace('.', '-').replace(' ', '-')
    extension = ".png"
    sistemaoperativo = str(os.name)
    print("so: " + sistemaoperativo)
    if sistemaoperativo == "linux" or sistemaoperativo == "linux2" or sistemaoperativo == "darwin" or sistemaoperativo == "posix" or sistemaoperativo == "mac" or sistemaoperativo == "os2" or sistemaoperativo == "cygwin":
        #para so basado en linux, mac os, etc.
        ruta = str(pathlib.Path().absolute()) + "/departamentos/static/img/grafico"
    else:
        #para windows
        ruta = str(pathlib.Path().absolute()) + "\\departamentos\\static\\img\\grafico"
    # guardar fichero
    # plt.show()
    enlace_completo = ruta + nombre_fichero + extension
    plt.savefig(enlace_completo)
    plt.close()

    nombre_fichero = "grafico" + nombre_fichero


    # devolver la ruta
    return str(nombre_fichero + extension)

def func(pct, allvals):
    absolute = int(np.round(pct / 100. * np.sum(allvals)))
    return "{:.1f}%\n({:d})".format(pct, absolute)

def ranking_sueldos():
    # create data
    nominas = Nomina.objects.all().order_by('-cantidad')

    try:

        # create a dataset
        height = []
        bars = ()
        numero = 1
        for nominas in nominas:
            height.append(nominas.cantidad)
            bars = bars + ("Trabajador " + str(numero),)
            numero = numero + 1


        x_pos = np.arange(len(bars))

        # Create bars
        plt.bar(x_pos, height, color=(0.2, 0.4, 0.6, 0.6))

        # Create names on the x-axis
        plt.xticks(x_pos, bars)

        # Show graph
        # plt.show()

    except:
        return "Error"

    return generar_archivo()

def cuantos_partes_por_cada_proyecto():
    proyectos = Proyecto.objects.all()
    height = []
    bars = ()
    for proyecto in proyectos:
        partes = Parte.objects.filter(proyecto=proyecto)
        height.append(partes.count())
        bars = bars + (proyecto.nombre,)

    y_pos = np.arange(len(bars))

    # Create bars
    plt.barh(y_pos, height)

    # Create names on the x-axis
    plt.yticks(y_pos, bars)

    return generar_archivo()
