#!/usr/bin/python3
# -*- coding: utf-8 -*-

import sys
class Calculadora():

  def __init__(self, valor1,valor2):
    "Esto es el método iniciliazador"
    self.valor1 = valor1
    self.valor2 = valor2

  def suma(self):
    return self.valor1+self.valor2
   

  def resta(self):
    return self.valor1-self.valor2

class CalculadoraHija(Calculadora):

  def multiplica(self):
    return self.valor1*self.valor2
   
  def divide(self):
    try:
        return self.valor1/self.valor2
    except ZeroDivisionError:
        sys.exit('Division by zero is not allowed')
    
if __name__ == "__main__":
    if len(sys.argv) !=4:
        sys.exit('Se usa así: python3 calcoo.py operando1 operador operando2')

    Op1=CalculadoraHija(int(sys.argv[1]),int(sys.argv[3]))

    if sys.argv[2] == "suma":
        resul = Op1.suma()
    elif sys.argv[2] == "resta":
        resul = Op1.resta()
    elif sys.argv[2] == "multiplica":
        resul = Op1.multiplica()
    elif sys.argv[2] == "divide":
        resul = Op1.divide()
    else:
        sys.exit('Operación sólo suma o resta')
print (resul)
