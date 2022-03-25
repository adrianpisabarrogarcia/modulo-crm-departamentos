from departamento import Departamento

class Permiso():
    id = ""
    escritura = False
    departamento = Departamento()

    def __init__(self, id, escritura, departamento):
        self.id = id
        self.escritura = escritura
        self.departamento = departamento



    #Getters & Setters
    def getId(self):
        return self.id

    def setId(self, id):
        self.id = id

    def getEscritura(self):
        return self.escritura

    def setEscritura(self, escritura):
        self.escritura = escritura

    def getDepartamento(self):
        return self.departamento

    def setDepartamento(self, departamento):
        self.departamento = departamento


    #To json
    def toJson(self):
        return {
            "id": self.id,
            "escritura": self.escritura,
            "departamento": self.departamento.toJson()
        }

    #To String
    def __str__(self):
        return "Permiso: " + self.id + " - " + str(self.escritura) + " - " + str(self.departamento)

    #From Json
    @staticmethod
    def fromJson(json):
        return Permiso(
            json["id"],
            json["escritura"],
            Departamento.fromJson(json["departamento"])
        )

