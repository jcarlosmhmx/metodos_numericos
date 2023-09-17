#!/usr/bin/env python

def f(x):
    return 0.95 * x**3 - 5.9 * x**2 + 10.9 * x - 6

def f_prime(x):
    return 2.85 * x**2 - 11.8 * x + 10.9

def newton_raphson(x0, iterations):
    for _ in range(iterations):
        
        x0 = x0 - f(x0) / f_prime(x0)
    return x0

# Suponiendo un valor inicial cercano a la raíz real más grande
valor_inicial = 3.0
iteraciones = 3

raiz_aproximada = newton_raphson(valor_inicial, iteraciones)
print(f"La raíz aproximada es: {raiz_aproximada}")
