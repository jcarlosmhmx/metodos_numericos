#!/usr/bin/env python
def f(x):
    return 0.95 * x**3 - 5.9 * x**2 + 10.9 * x - 6

def secante(x0, x1, delta, max_iter=100):
    
    #Agregamos el header:
    print("Index\tx0\tf(x0)\tx1\tf(x1)\tx2")
    i=0
    for i in range(max_iter):
        f_x1 = f(x1)
        f_x0 = f(x0)
        if abs(f_x1 - f_x0) < delta:
            return x1
        
        x2 = x1 - f_x1 * (x1 - x0) / (f_x1 - f_x0)

        print(i, "\t", x0,"\t", f(x0), "\t",x1,"\t",f(x1), "\t",x2 )
        
        x0, x1 = x1, x2
    
    raise Exception(f"No se alcanzó la convergencia deseada después de {max_iter} iteraciones")

# Valores iniciales
x0 = 3.5
x1 = x0 + 0.01  # Se añade delta a x0 para obtener x1
delta = 0.01

# Calcula la raíz
raiz = secante(x0, x1, delta)
print("----------------------------------------------------------------------------")
print(f"La raíz aproximada es: {raiz}")
print("----------------------------------------------------------------------------")

