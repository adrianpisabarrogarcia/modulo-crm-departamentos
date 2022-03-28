class Departamento():
    id = ""
    nombre = ""


    def __init__(self, id, nombre):
        self.id = id
        self.nombre = nombre


    # Getters & Setters
    def getId(self):
        return self.id

    def setId(self, id):
        self.id = id

    def getNombre(self):
        return self.nombre

    def setNombre(self, nombre):
        self.nombre = nombre



    # To json
    def toJson(self):
        return {
            "id": self.id,
            "nombre": self.nombre
        }

    # To String
    def __str__(self):
        return "Departamento: " + self.id + " " + self.nombre

    # From Json
    def fromJson(json):
        return Departamento(
            json["id"],
            json["nombre"]
        )


