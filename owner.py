#from menu import Menu
from contact import Contact
from person import Person


class Owner(Person):

    cedula = ""
    nombre = ""
    apellido = ""
    edad = 0
    correo_electronico = ""
    telefono = ""
    estado_civil = ""

    def __init__(self, cedula, nombre, apellido, edad, correo_electronico, telefono, estado_civil, contacts):
        self.cedula = cedula.upper()
        self.nombre = nombre.upper()
        self.apellido = apellido.upper()
        self.edad = edad
        self.correo_electronico = correo_electronico
        self.telefono = telefono
        self.estado_civil = estado_civil.upper()
        self.contacts = contacts

    def __str__(self):
        salida = "Datos del Propietario\n"
        salida = "Cedula: " + "\t\t" + self.cedula + "\n"
        salida = salida + "Nombre: " + "\t\t" + self.nombre.upper() + "\n"
        salida = salida + "Apellido: " + "\t\t" + self.apellido.upper() + "\n"
        salida = salida + "Edad: " + "\t\t\t" + str(self.edad) + "\n"
        salida = salida + "Correo Electrónico: " + "\t" + self.correo_electronico + "\n"
        salida = salida + "Telefono: " + "\t\t" + str(self.telefono) + "\n"
        salida = salida + "Estado Civil: " + "\t\t" + self.estado_civil.upper() + "\n"

        salida = salida + "\n CONTACTOS ASIGNADOS\n"
        for contact in self.contacts:
            salida = salida + contact.__str__() + "\n"

        return salida
