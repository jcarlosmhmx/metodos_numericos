#!/usr/bin/env python
#----------------------Funciones------------------------
def funcion(x):
    return  1-((g**2)/(g*((Ac(x))**3))*(3+x)) 
    
def Ac(x):
    return 3*x+((x**2)/2)

def falsaPosicion(a, b, tolerancia=0.9, max_iter=100):
    if funcion(a) * funcion(b) >= 0:
        raise ValueError("La función debe cambiar de signo en el intervalo [a, b]")
    index =0

    #Agregamos el header:
    print("Index\t a\t f(a)              \t b\t f(b)                \t c\t                    f(c)")

    for _ in range(max_iter):
        c = (a * funcion(b) - b * funcion(a)) / (funcion(b) - funcion(a))
        print (index,"\t",a,"\t",funcion(a),"\t",b,"\t",funcion(b),"\t",c,"\t",funcion(c))
        index = index +1
        if abs(funcion(c)) < tolerancia:
            return c

        if funcion(c) * funcion(a) < 0:
            b = c
        else:
            a = c

    raise Exception(f"No se alcanzó la tolerancia deseada después de {max_iter} iteraciones")




#----------------------Variables------------------------
#gravedad
g=9.81
#intervalo inicial
a=0.5
#intervalo final
b=2.5


# Ejemplo de uso:)
raiz = falsaPosicion(a,b, tolerancia=0.99)
print("----------------------------------------------------------------------------")
print(f"La raíz aproximada es: {raiz}")
print("----------------------------------------------------------------------------")