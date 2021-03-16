from tool import ImprimirMenu, buscarElemento, lee_entero
from direccion import Direccion
from contact import Contact
from owner import Owner
from os import read
import os
import time


ImprimirMenu()


def Menu():
    opcion = 0
    contactos = []
    contacts = {}
    cedula = ""
    nombre = ""
    apellido1 = ""
    apellido2 = ""
    edad = ""
    correo_electronico = ""
    telefono = ""
    estado_civil = ""
    pais = ""
    provincia = ""
    canton = ""

    print("CREAR UN PROPIETARIO\n")
    while cedula == "":
        cedula = input("Ingrese su cedula: ")
    while nombre == "":
        nombre = input("Ingrese su nombre: ")
    while apellido1 == "":
        apellido1 = input("Ingrese su apellido: ")
    while edad == "":
        edad = input("Ingrese su edad: ")
        edad = lee_entero(edad)

    while correo_electronico == "":
        correo_electronico = input("Ingrese su correo electrónico: ")
    while telefono == "":
        telefono = input("Ingrese su número de teléfono: ")
        telefono = lee_entero(telefono)
    while estado_civil == "":
        estado_civil = input("Ingrese su estado civil: ")

    my_owner = Owner(cedula, nombre, apellido1, edad,
                     correo_electronico, telefono, estado_civil, contacts)

    while (opcion != '9'):
        ImprimirMenu()
        opcion = input('Digite el numero de la opción que desea realizar: ')

        if (opcion == '1'):
            print("\n ========================================================================================= \n")
            print("Datos del propietario\n")
            print(my_owner)
            print("\n ================================ FIN ====================================================== \n")
            input("\n Presione la tecla Intro para continuar")

        elif (opcion == '2'):
            cedula = ""
            nombre = ""
            apellido1 = ""
            apellido2 = ""
            edad = ""
            correo_electronico = ""
            telefono = ""
            estado_civil = ""
            pais = ""
            provincia = ""
            canton = ""

            print("Ingresar un contacto a mi lista")

            print("CREAR UN CONTACTO\n")
            while cedula == "":
                cedula = input("Ingrese la cedula: ")
            while nombre == "":
                nombre = input("Ingrese el nombre: ")
            while apellido1 == "":
                apellido1 = input("Ingrese el primer apellido: ")
            while apellido2 == "":
                apellido2 = input("Ingrese el segundo apellido: ")
            while edad == "":
                edad = input("Ingrese la edad: ")
                edad = lee_entero(edad)
            while correo_electronico == "":
                correo_electronico = input("Ingrese el correo electrónico: ")
            while telefono == "":
                telefono = input("Ingrese el número de teléfono: ")
                telefono = lee_entero(telefono)
            while estado_civil == "":
                estado_civil = input("Ingrese su estado civil: ")

            print("\nDireccion")
            while pais == "":
                pais = input("Ingrese el pais: ")
            while provincia == "":
                provincia = input("Ingrese la provincia: ")
            while canton == "":
                canton = input("Ingrese el canton: ")

            direccion = Direccion(pais, provincia, canton)

            my_contact = Contact(
                cedula, nombre, apellido1, apellido2, edad,
                correo_electronico, telefono, direccion)

            contactos.append(my_contact)
            #contacts[cedula] = my_contact
            my_owner.contacts[cedula] = my_contact

            input(
                "\n Contacto registrado correctamente, presione cualquier tecla para continuar")

        elif (opcion == '3'):
            valor = input("Ingrese el Nombre o el Apellido a buscar: ")
            resultado = buscarElemento(valor.upper(), contactos)
            if resultado != None:
                print(resultado)
            input("\n Presione la tecla Intro para continuar")

        elif (opcion == '4'):

            print(" Eliminar un contacto de mi lista")
            valor = input("Ingrese el Nombre o el Apellido a buscar: ")
            resultado = buscarElemento(valor.upper(), contactos)
            if resultado != None:
                print(resultado)
                cedula = input(
                    "Ingrese la cédula para confirmar la eliminación: ")
                if cedula == my_owner.cedula:
                    contactos.remove(resultado)

            input("\n Presione la tecla Intro para continuar")

        elif (opcion == '5'):
            print("Ver la lista de contactos")
            for contacto in contactos:
                print(contacto)
            input("\n Presione la tecla Intro para continuar")

        elif (opcion == '6'):

            print("\n ¡¡¡ Gracias por Utilizar nuestra aplicación !!!")
            break
        else:
            print("Opción no válida")
            time.sleep(3)
            borrarPantalla


Menu()
