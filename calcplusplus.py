#!/usr/bin/python3
# -*- coding: utf-8 -*-

import sys
import csv
from calcoohija import CalculadoraHija

with open(sys.argv[1], 'r') as fich:
    lineas = csv.reader(fich)

    for operaciones in lineas:
        operador = operaciones[0]  # ["suma", 1, 2, 3, 4, 5] -> "suma"
        resul = int(operaciones[1])  # ["suma", 1, 2, 3, 4, 5] -> 1

        lista = []
        for numero in operaciones[1:]:
            try:
                numero = int(numero)
                lista.append(numero)
            except ValueError:
                sys.exit("Error: No numero")

        if operador == 'suma':
            for operando in lista[1:]:
                op = CalculadoraHija(resul,operando)
                resul = op.suma()
            print(resul)

        elif operador == 'resta':
            for operando in lista[1:]:
                op = CalculadoraHija(resul,operando)
                resul = op.resta()
            print(resul)
        if operador == 'multiplica':
            for operando in lista[1:]:
                op = CalculadoraHija(resul,operando)
                resul = op.multiplica()
            print(resul)

        elif operador == 'divide':
            for operando in lista[1:]:
                op = CalculadoraHija(resul,operando)
                resul = op.divide()
            print(resul)
