class Person:
    cedula = ""
    nombre = ""
    primer_apellido = ''
    edad = 0
    correo_electronico = ""
    telefono = ""

    def __init__(self, cedula, nombre, primer_apellido, edad, correo_electronico, telefono):
        self.cedula = cedula
        self.nombre = nombre.upper()
        self.primer_apellido = primer_apellido.upper()
        self.edad = edad
        self.correo_electronico = correo_electronico
        self.telefono = telefono

    def __str__(self):
        return '{} {} {}'.format(self.cedula, self.nombre, self.primer_apellido)
