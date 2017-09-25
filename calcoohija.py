#!/usr/bin/python3
# -*- coding: utf-8 -*-

import sys
from calcoo import Calculadora

class CalculadoraHija(Calculadora):  

  def multiplica(self):
    return self.valor1*self.valor2
   
  def divide(self):
    try:
        return self.valor1/self.valor2
    except ZeroDivisionError:
        sys.exit('Division by zero is not allowed')
    
if __name__ == "__main__":
#    if len(sys.argv) !=4:
#        sys.exit('Se usa así: python3 calcoo.py operando1 operador operando2')

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
        sys.exit('Operación sólo suma, resta, multiplica o divide')
print (resul)
