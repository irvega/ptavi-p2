#!/usr/bin/python3
# -*- coding: utf-8 -*-

import sys
import csv
from calcoohija import CalculadoraHija

with open(sys.argv[1],'r') as fich:
    lineas=csv.reader(fich)
    
    for operaciones in lineas:
        operador=operaciones[0] # ["suma", 1, 2, 3, 4, 5] -> "suma"
        resul = int(operaciones[1]) # ["suma", 1, 2, 3, 4, 5] -> 1

        if operador=='suma':
            for operando in operaciones[2:]:
                resul += int(operando)
            print(resul)

        elif operador=='resta':
            for operando in operaciones[2:]:
                resul -= int(operando)
            print(resul)
        if operador=='multiplica':
            for operando in operaciones[2:]:
                resul *= int(operando)
            print(resul)

        elif operador=='divide':
            for operando in operaciones[2:]:
                try:
                    resul /= int(operando)                    
                except ZeroDivisionError:
                    sys.exit('  Division by zero is not allowed')
            print(resul)

