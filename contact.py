from direccion import Direccion
from os import name
from person import Person

cedula = ""
segundo_apellido = ""
direccion = Direccion("", "", "")


class Contact(Person, Direccion):
    def __init__(self, cedula, nombre, primer_apellido, segundo_apellido, edad, correo_electronico, telefono, direccion):

        self.segundo_apellido = segundo_apellido.upper()
        self.direccion = direccion
        Person.__init__(self, cedula, nombre, primer_apellido, edad,
                        correo_electronico, telefono)

    def __str__(self):
        salida = "Datos del Contacto\n"
        salida = "Cedula: \t\t" + self.cedula + "\n"
        salida = salida + "Nombre: \t\t" + self.nombre + "\n"
        salida = salida + "Primer Apellido: \t" + self.primer_apellido + "\n"
        salida = salida + "Segundo Apellido: \t" + self.segundo_apellido + "\n"
        salida = salida + "Edad: \t\t\t" + str(self.edad) + "\n"
        salida = salida + "Correo Electrónico: \t" + self.correo_electronico + "\n"
        salida = salida + "Telefono: \t\t" + str(self.telefono) + "\n"
        salida = salida + "Pais: \t\t\t" + self.direccion.nombrePais + "\n"
        salida = salida + "Provincia: \t\t" + self.direccion.nombreProvincia + "\n"
        salida = salida + "Canton: \t\t" + self.direccion.nombreCanton + "\n"
        return salida
