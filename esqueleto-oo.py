#!/usr/bin/python3
# -*- coding: utf-8 -*-


class Clase(ClaseMadre):
    "Esto es un ejemplo de clase que hereda de ClaseMadre"


def __init__(self, valor1, valor2):
        "Esto es el método iniciliazador"
        self.valor1 = valor1
        self.valor2 = valor2


def suma(self):
        resul = self.valor1+self.valor2

if __name__ == "__main__":
    objeto = Clase("pepe")  # Creo un objeto de la clase Clase
# y le paso el valor pepe para su
# atributo en la inicialización
