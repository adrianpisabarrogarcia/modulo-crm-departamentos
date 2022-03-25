from nomina import Nomina

class Usuario():
    id = ""
    permisos = []
    nombre = ""
    username = ""
    password = ""
    email = ""
    habilitado = True
    nomina = Nomina()


    def __init__(self, id, permisos, nombre, username, password, email, habilitado, nomina):
        self.id = id
        self.permisos = permisos
        self.nombre = nombre
        self.username = username
        self.password = password
        self.email = email
        self.nomina = nomina


    #Getters & Setters
    def getId(self):
        return self.id

    def setId(self, id):
        self.id = id

    def getPermisos(self):
        return self.permisos

    def setPermisos(self, permisos):
        self.permisos = permisos

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

    def getNomina(self):
        return self.nomina

    def setNomina(self, nomina):
        self.nomina = nomina



    #To json

    def toJSON(self):
        return {
            'id': self.id,
            'permisos': self.permisos,
            'nombre': self.nombre,
            'username': self.username,
            'password': self.password,
            'email': self.email,
            'habilitado': self.habilitado,
            'nomina': self.nomina.toJson()
        }

    #From Json
    def fromJSON(json):
        usuario = Usuario()
        usuario.id = json['id']
        usuario.permisos = json['permisos']
        usuario.nombre = json['nombre']
        usuario.username = json['username']
        usuario.password = json['password']
        usuario.email = json['email']
        usuario.habilitado = json['habilitado']
        usuario.nomina = Nomina.fromJson(json['nomina'])
        return usuario

    #To String
    def __str__(self):
        return "Usuario: " + self.id + " " + self.nombre + " " + self.username + " " + self.password + " " + self.email + " " + self.habilitado + " " + self.nomina.toString()