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
    
    #Agregamos el header:
    print("Index\t a\t f(a)              \t b\t f(b)                \t c\t f(c)")

    while(b-a):
        index=index+1
        c=(a+b)/2
        print (index,"\t",a,"\t",funcion(a),"\t",b,"\t",funcion(b),"\t",c,"\t",funcion(c))


        if funcion(c)==0:
            return c
        elif funcion(c)*funcion(a) <0:
            b=c
        else:
            a=c
    return (a+b)/2

def raiz(a,b,tolerancia):
    if funcion(a) * funcion(b) >= 0:
        raise ValueError("La función debe cambiar de signo en el intervalo [a, b].")
    
    while (b - a) >= tolerancia:
        c = (a + b) / 2
        if funcion(c) == 0.0:
            return c
        elif funcion(c) * funcion(a) < 0:
            b = c
        else:
            a = c

    return (a + b) / 2
#----------------------Variables------------------------
#gravedad
g=9.81
#intervalo inicial
a=0.5
#intervalo final
b=2.5
#tolerancia
tolerancia = 0.99

biseccion(a,b,tolerancia)
print("\n La raiz es aproximada es: ",raiz(a,b,tolerancia))