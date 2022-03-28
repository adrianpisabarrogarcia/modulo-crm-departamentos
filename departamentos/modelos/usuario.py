from departamentos.modelos.nomina import Nomina

class Usuario():
    id = ""
    nombre = ""
    username = ""
    password = ""
    email = ""
    habilitado = True

    def __init__(self, id, nombre, username, password, email, habilitado):
        self.id = id
        self.nombre = nombre
        self.username = username
        self.password = password
        self.email = email
        self.habilitado = habilitado

    #Getters & Setters
    def getId(self):
        return self.id

    def setId(self, id):
        self.id = id

    def getNombre(self):
        return self.nombre

    def setNombre(self, nombre):
        self.nombre = nombre

    def getUsername(self):
        return self.username

    def setUsername(self, username):
        self.username = username

    def getPassword(self):
        return self.password

    def setPassword(self, password):
        self.password = password

    def getEmail(self):
        return self.email

    def setEmail(self, email):
        self.email = email

    def getHabilitado(self):
        return self.habilitado

    def setHabilitado(self, habilitado):
        self.habilitado = habilitado



    #To json
    def toJSON(self):
        return {
            'id': self.id,
            'nombre': self.nombre,
            'username': self.username,
            'password': self.password,
            'email': self.email,
            'habilitado': self.habilitado,
        }

    #From Json
    def fromJSON(json):
        return Usuario(json['id'], json['nombre'] , json['username'] , json['password'] , json['email'], json['habilitado'])

    #To String
    def __str__(self):
        return "Usuario: " + self.id + " " + self.nombre + " " + self.username + " " + self.password + " " + self.email + " " + self.habilitado