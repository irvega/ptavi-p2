#!/usr/bin/python3
# -*- coding: utf-8 -*-

import sys
import csv
from calcoohija import CalculadoraHija

if len(sys.argv) != 2:
    sys.exit("  Use: python3 calcplusplus.py <fich>")

with open(sys.argv[1], 'r') as fich:

    lineas = csv.reader(fich)

    for operaciones in lineas:

        lista = []
        for numero in operaciones[1:]:
            try:
                numero = int(numero)
                lista.append(numero)
            except ValueError:
                sys.exit("Error: Not number")

        if len(lista) == 0:
            resul = 0
        else:
            resul = int(operaciones[1])  # ["suma", 1, 2, 3, 4, 5] -> 1

        operador = operaciones[0]  # ["suma", 1, 2, 3, 4, 5] -> "suma"

        if operador == 'suma':
            for operando in lista[1:]:
                op = CalculadoraHija(resul, operando)
                resul = op.suma()

        elif operador == 'resta':
            for operando in lista[1:]:
                op = CalculadoraHija(resul, operando)
                resul = op.resta()
        if operador == 'multiplica':
            for operando in lista[1:]:
                op = CalculadoraHija(resul, operando)
                resul = op.multiplica()

        elif operador == 'divide':
            for operando in lista[1:]:
                op = CalculadoraHija(resul, operando)
                resul = op.divide()
        print(resul)
