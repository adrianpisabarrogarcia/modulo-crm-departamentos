
class Parte():
    id = ""
    id_usuario = ""
    proyecto = ""
    observacion = ""
    duracion = ""
    fecha = ""

    def __init__(self, id, id_usuario, proyecto, observacion, duracion, fecha):
        self.id = id
        self.id_usuario = id_usuario
        self.proyecto = proyecto
        self.observacion = observacion
        self.duracion = duracion
        self.fecha = fecha


    #Getters & Setters
    def getId(self):
        return self.id

    def setId(self, id):
        self.id = id

    def getIdUsuario(self):
        return self.id_usuario

    def setIdUsuario(self, id_usuario):
        self.id_usuario = id_usuario

    def getProyecto(self):
        return self.proyecto

    def setProyecto(self, proyecto):
        self.proyecto = proyecto

    def getObservacion(self):
        return self.observacion

    def setObservacion(self, observacion):
        self.observacion = observacion

    def getDuracion(self):
        return self.duracion

    def setDuracion(self, duracion):
        self.duracion = duracion

    def getFecha(self):
        return self.fecha

    def setFecha(self, fecha):
        self.fecha = fecha


    #To json
    def toJSON(self):
        return {
            "id": self.id,
            "id_usuario": self.id_usuario,
            "proyecto": self.proyecto,
            "observacion": self.observacion,
            "duracion": self.duracion,
            "fecha": self.fecha
        }

    #To String
    def __str__(self):
        return "Parte: {}, Id usuario: {}, Proyecto: {}, Observacion: {}, Duracion: {}, Fecha: {}".format(self.id, self.id_usuario, self.proyecto, self.observacion, self.duracion, self.fecha)

    #From Json
    @staticmethod
    def fromJSON(json):
        return Parte(
            json["id"],
            json["id_usuario"],
            json["proyecto"],
            json["observacion"],
            json["duracion"],
            json["fecha"]
        )

