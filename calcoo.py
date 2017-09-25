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
    
if __name__ == "__main__":
    Op1=Calculadora(2,7)
    resul=Op1.suma()
print (resul)
