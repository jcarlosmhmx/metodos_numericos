#!/usr/bin/env python
#----------------------------Funciones----------------
def evaluar(x):
    return(-185*x)+1650.015

def raizExiste(xl,xu):
    if evaluar(xl)*evaluar(xu)<0:
        print ("Existe la raiz")
    else:
        print ("La raiz no existe")

def calcularXr(xl,xu):
    return (xl+xu)/2

def calcularError(xr, xranterior):
    return ((xr-xranterior)/xr)*100

#---------------------------variables-----------------
xl = 0.0
xu = 12.0
xr = 0.0
error = 0.0
xranterior = 0.0
terminar = 0
i = 1
#-------------------------código----------------------

raizExiste(xl,xu)
print("\n\t\tNtXR\tI[:]\t\tError")
while terminar != 1:
    xr = calcularXr(xl,xu)
    if i != 1:
        error = calcularError(xr, xranterior)
        if error < 0:
            error = error*-1
        if error == 0:
            terminar = 1
        print("\n\t\t",i,"\t",xr,"\t",xl,xu,"\t",error,"%")
    else:
        print("\n\t\t",i,"\t",xr,"\t",xl,xu,"\t")
    if evaluar(xr)*evaluar(xl)<0:
        xu = xr
    if evaluar(xr)*evaluar(xl)>0:
        xl = xr
    xranterior = xr
    i+=1
print("----------------------------------------------------------------------------")
print("\t La posición donde no hay momento es ",xr )
print("----------------------------------------------------------------------------")


























