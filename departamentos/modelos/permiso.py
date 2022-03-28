from departamentos.modelos.departamento import Departamento

class Permiso():
    id_usuario = ""
    escritura = False
    id_departamento = ""

    def __init__(self, id_usuario, escritura, id_departamento):
        self.id_usuario = id_usuario
        self.escritura = escritura
        self.id_departamento = id_departamento



    #Getters & Setters
    def getIdUsuario(self):
        return self.id_usuario

    def setIdUsuario(self, id_usuario):
        self.id_usuario = id_usuario

    def getEscritura(self):
        return self.escritura

    def setEscritura(self, escritura):
        self.escritura = escritura

    def getIdDepartamento(self):
        return self.id_departamento

    def setIdDepartamento(self, id_departamento):
        self.id_departamento = id_departamento



    #To json
    def toJSON(self):
        return {
            "id_usuario": self.id_usuario,
            "escritura": self.escritura,
            "id_departamento": self.id_departamento
        }

    #To String
    def __str__(self):
        return "Permiso: " + self.id_usuario + " " + str(self.escritura) + " " + self.id_departamento

    #From Json
    @staticmethod
    def fromJSON(json):
        return Permiso(
            json["id_usuario"],
            json["escritura"],
            json["id_departamento"]
        )

