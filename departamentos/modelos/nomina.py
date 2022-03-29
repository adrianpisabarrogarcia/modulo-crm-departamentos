class Nomina():
    id_usuario = ""
    cantidad = ""
    fecha = ""

    def __init__(self, id_usuario, cantidad, fecha):
        self.id_usuario = id_usuario
        self.cantidad = cantidad
        self.fecha = fecha

    # Getters & Setters
    def get_id_usuario(self):
        return self.id_usuario

    def set_id_usuario(self, id_usuario):
        self.id_usuario = id_usuario

    def getCantidad(self):
        return self.cantidad

    def setCantidad(self, cantidad):
        self.cantidad = cantidad

    def getFecha(self):
        return self.fecha

    def setFecha(self, fecha):
        self.fecha = fecha

    # To String
    def __str__(self):
        return "Id usuario: " + self.id_usuario + " Cantidad: " + self.cantidad + " Fecha: " + self.fecha

    # To Json
    def toJSON(self):
        return {
            'id_usuario': self.id_usuario,
            'cantidad': self.cantidad,
            'fecha': self.fecha
        }

    # From Json
    def fromJSON(json):
        return Nomina(json["id_usuario"], json["cantidad"], json["fecha"])
