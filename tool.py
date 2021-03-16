import os
import time


def lee_entero(entrada):
    while True:
        try:
            entrada = int(entrada)
            return entrada
        except ValueError:
            print("La entrada es incorrecta: escribe un numero entero")
            entrada = input("Escribe un numero entero: ")


def buscarElemento(elemento, Lista):
    for item in Lista:
        if item.nombre == elemento or item.primer_apellido == elemento or item.segundo_apellido == elemento:
            return item


def borrarPantalla():  # Definimos la función estableciendo el nombre que queramos
    if os.name == "posix":
        os.system("clear")
    elif os.name == "ce" or os.name == "nt" or os.name == "dos":
        os.system("cls")


def ImprimirMenu():
    borrarPantalla()
    print("\033[2J\033[1;1f")  # Borrar pantalla y situar cursor
    print("\n ========================================================================================= \n")
    print("\033[;36m"+"Bienvenido al sistema de Agenda\n")
    print("\033[;36m"+"Seleccione una Opción\n")
    print("\033[4;35m"+"1- Ver mis datos")
    print("\033[4;35m"+"2- Agregar Contacto")
    print("\033[4;35m"+"3- Buscar un contacto por nombre ó por apellido ")
    print("\033[4;35m"+"4- Eliminar un contacto de mi lista")
    print("\033[4;35m"+"5- Ver la lista de contactos")
    print("\033[1;33m"+"6- Terminar")
    print("\n")
