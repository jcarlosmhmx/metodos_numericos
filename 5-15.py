#!/usr/bin/env python
#----------------------Funciones------------------------
def funcion(x):
    return  1-((g**2)/(g*((Ac(x))**3))*(3+x)) 
    #return x**2 - 4
    

def Ac(x):
    return 3*x+((x**2)/2)

def biseccion(a, b, tolerancia):
    index=0
    if funcion(a) * funcion(b) >= 0:
        raise("Error: La función debe cambiar de signo en el intervalo [a,b]")
    
    while(b-a):
        index=index+1
        c=(a+b)/2
        print (index," ",a," ",funcion(a)," ",b," ",funcion(b)," ",c," ",funcion(c))


        if funcion(c)==0:
            return c
        elif funcion(c)*funcion(a) <0:
            b=c
        else:
            a=c
    return (a+b)/2
#----------------------Variables------------------------
g=9.81

x=1

#intervalo inicial
a=0.5
#intervalo final
b=2.5
#tolerancia
tolerancia = 0.00001


biseccion(a,b,tolerancia)