#!/usr/bin/env python
#----------------------------Funciones----------------
def evaluar(x):
    return(-185*x)+1650.015

def raizExiste(xl,xu):
    if evaluar(xl)*evaluar(xu)<0:
        print ("Existe la raiz")
    else:
        print ("La raiz no existe")

#---------------------------variables-----------------
xl = 0.0
xu = 12.0
xr = 0.0
error = 0.0
xranterior = 0.0

#-------------------------código----------------------

raizExiste(xl,xu)

























