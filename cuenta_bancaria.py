import os
from random import randint


class Persona:
    def __init__(self,nombre,apellido):
        self.nombre = nombre
        self.apellido = apellido


class Cliente(Persona):
    numero_cuenta = 444333222111
    balance = 10000

    def __init__(self, nombre,apellido,numero_cuenta, balance):
        super().__init__(nombre,apellido)       # Definir atributos de la clase padre, ya que hereda de ésta
        self.numero_cuenta = numero_cuenta
        self.balance = balance

    def imprimir(self):
        print(self.nombre)
        print(self.apellido)
        print("Numero de cuenta" + str(self.numero_cuenta))
        print(f"{self.balance}€\n")

    def depositar(self,cantidad):
        self.balance += cantidad

    def retirar(self,cantidad):
        if self.balance > cantidad:
            self.balance -= cantidad
        else:
            print("No tiene suficiente dinero")


def crear_cliente():
    nombre = input("Nombre: ")
    apellido = input("Apellido: ")
    numero_cuenta = randint(10000,99999)
    balance = 0
    return Cliente(nombre,apellido,numero_cuenta,balance)


def inicio(cliente):
    salir = False
    while not salir:
        print("1. Retirar")
        print("2. Depositar")
        print("3. imprimir datos")
        print("0. Salir")
        res = input("Opción: ")
        match res:
            case '1':
                cantidad = int(input("Cantidad a retirar: "))
                cliente.retirar(cantidad)
                cliente.imprimir()
            case '2':
                cantidad = int(input("Cantidad a retirar: "))
                cliente.depositar(cantidad)
                cliente.imprimir()
            case '3':
                cliente.imprimir()
            case '0':
                salir=True
        os.system('cls')


cliente = crear_cliente()
inicio(cliente)