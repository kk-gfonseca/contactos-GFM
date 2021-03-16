class Direccion:

    nombrePais = "Costa Rica"
    nombreProvincia = ""
    nombreCanton = ""

    def __init__(self, nombrePais, nombreProvincia, nombreCanton):
        self.nombrePais = nombrePais.upper()
        self.nombreProvincia = nombreProvincia.upper()
        self.nombreCanton = nombreCanton.upper()

    def __str__(self):
        return ('{} {} {}'.format(self.nomrePais, self.nombreProvincia, self.nombreCanton))
