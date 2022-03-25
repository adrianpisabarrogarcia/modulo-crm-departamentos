class Nomina():
    id = ""
    cantidad = ""
    fecha = ""

    def __init__(self, id, cantidad, fecha):
        self.id = id
        self.cantidad = cantidad
        self.fecha = fecha


    #Getters & Setters
    def getId(self):
        return self.id

    def setId(self, id):
        self.id = id

    def getCantidad(self):
        return self.cantidad

    def setCantidad(self, cantidad):
        self.cantidad = cantidad

    def getFecha(self):
        return self.fecha

    def setFecha(self, fecha):
        self.fecha = fecha


    #To String
    def __str__(self):
        return "ID: " + self.id + " Cantidad: " + self.cantidad + " Fecha: " + self.fecha

    #To Json
    def toJson(self):
        return {
            "id": self.id,
            "cantidad": self.cantidad,
            "fecha": self.fecha
        }

    #From Json
    def fromJson(json):
        return Nomina(json["id"], json["cantidad"], json["fecha"])





