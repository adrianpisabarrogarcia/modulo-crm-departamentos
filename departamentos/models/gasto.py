class Gasto():
    id = ""
    nombre = ""
    precio = 0.0
    cantidad = 0
    fecha = ""

    def __init__(self, id, nombre, precio, cantidad, fecha):
        self.id = id
        self.nombre = nombre
        self.precio = precio
        self.cantidad = cantidad
        self.fecha = fecha


    #Getters & Setters
    def getId(self):
        return self.id

    def setId(self, id):
        self.id = id

    def getNombre(self):
        return self.nombre

    def setNombre(self, nombre):
        self.nombre = nombre

    def getPrecio(self):
        return self.precio

    def setPrecio(self, precio):
        self.precio = precio

    def getCantidad(self):
        return self.cantidad

    def setCantidad(self, cantidad):
        self.cantidad = cantidad

    def getFecha(self):
        return self.fecha

    def setFecha(self, fecha):
        self.fecha = fecha




    #To json
    def toJson(self):
        return {
            "id": self.id,
            "nombre": self.nombre,
            "precio": self.precio,
            "cantidad": self.cantidad,
            "fecha": self.fecha
        }

    #To String
    def __str__(self):
        return "Gasto: " + self.nombre + " - " + str(self.precio) + " - " + str(self.cantidad) + " - " + self.fecha

    #From Json
    @staticmethod
    def fromJson(json):
        return Gasto(json["id"], json["nombre"], json["precio"], json["cantidad"], json["fecha"])
