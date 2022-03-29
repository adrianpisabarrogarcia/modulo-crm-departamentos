from proyecto import Proyecto

class Parte():
    id = ""
    proyecto = Proyecto()
    observacion = 0.0
    duracion = ""

    def __init__(self, id, proyecto, observacion, duracion):
        self.id = id
        self.proyecto = proyecto
        self.observacion = observacion
        self.duracion = duracion


    #Getters & Setters
    def getId(self):
        return self.id

    def setId(self, id):
        self.id = id

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


    #To json
    def toJSON(self):
        return {
            "id": self.id,
            "proyecto": self.proyecto.toJson(),
            "observacion": self.observacion,
            "duracion": self.duracion
        }

    #To String
    def __str__(self):
        return "Parte: {}, Proyecto: {}, Observacion: {}, Duracion: {}".format(self.id, self.proyecto, self.observacion, self.duracion)

    #From Json
    @staticmethod
    def fromJSON(json):
        return Parte(
            json["id"],
            Proyecto.fromJson(json["proyecto"]),
            json["observacion"],
            json["duracion"]
        )

