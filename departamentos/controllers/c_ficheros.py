import pathlib
from datetime import datetime
import json


#generar un log con un archivo concreto
def generar_logs(mensaje):
    now = datetime.now()

    #cada día se genera un archivo de log
    f = open(str(pathlib.Path().absolute())+"/departamentos/files/logs/"+now.strftime("%Y%m%d")+".log", 'a', encoding='utf-8')
    try:
        f.write("\n[INFO - "+ now.strftime("%H:%M:%S") +"] - " + mensaje)
    finally:
        f.close()

#función para leer un archivo json
def leer_archivos(nombre_archivo):
    file = open(str(pathlib.Path().absolute())+"/departamentos/files/"+nombre_archivo, 'r', encoding='utf-8')
    try:
        with file as f:
            #load json file
            jsonObject = json.load(f)
            f.close()
            generar_logs("Se ha leido el archivo: " + nombre_archivo)
            return jsonObject
    except FileNotFoundError:
        generar_logs("Archivo no encontrado: " + nombre_archivo)
        return []
    finally:
        generar_logs("Se ha cerrado el archivo: " + nombre_archivo)
        file.close()

#función para escribir un archivo json
def guardar_archivo(objeto, nombre_archivo):
    try:
        with open(str(pathlib.Path().absolute())+"/departamentos/files/"+nombre_archivo, 'w', encoding='utf-8') as f:
            json.dump(objeto, f)
            generar_logs("Se han guardado los datos en: " + nombre_archivo)
    except FileNotFoundError:
        generar_logs("Archivo no encontrado: " + nombre_archivo)
        return False
    finally:
        generar_logs("Se ha cerrado el archivo: " + nombre_archivo)
        f.close()
    return True





