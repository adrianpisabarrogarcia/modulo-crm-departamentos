class Nomina():
    cantidad = ""
    fecha = ""

    def __init__(self, cantidad, fecha):
        self.cantidad = cantidad
        self.fecha = fecha


    #Getters & Setters

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
        return " Cantidad: " + self.cantidad + " Fecha: " + self.fecha

    #To Json
    def toJson(self):
        return {
            'cantidad': self.cantidad,
            'fecha': self.fecha
        }

    #From Json
    def fromJson(json):
        return Nomina(json["cantidad"], json["fecha"])





