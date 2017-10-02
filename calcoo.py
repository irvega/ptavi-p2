#!/usr/bin/python3
# -*- coding: utf-8 -*-

import sys


class Calculadora():

    def __init__(self, valor1, valor2):
        "Esto es el método iniciliazador"
        self.valor1 = valor1
        self.valor2 = valor2

    def suma(self):
        return self.valor1+self.valor2

    def resta(self):
        return self.valor1-self.valor2

if __name__ == "__main__":
    if len(sys.argv) != 4:
        sys.exit('  Usar así: python3 calcoo.py operando1 operador operando2')
    try:
        operando1 = int(sys.argv[1])
        operando2 = int(sys.argv[3])
    except ValueError:
        sys.exit('  Operando1 y Operando2 deben ser numeros enteros')

    Op1 = Calculadora(int(sys.argv[1]), int(sys.argv[3]))

    if sys.argv[2] == "suma":
        resul = Op1.suma()
    elif sys.argv[2] == "resta":
        resul = Op1.resta()
    else:
        sys.exit('  Operación sólo "suma" o "resta"')
    print(resul)
