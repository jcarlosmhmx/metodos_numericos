#!/usr/bin/env python
"""
Este módulo Plantea el sistema de ecuaciones para el caso planteado y resuélvelo aplicando los métodos Simpson y Romberg 
encuentra la solución programando cada método. (Ver página 647, ejercicio 21.23) 
Author: Equipo 8 Métodos Numéricos
Fecha: Octubre 8, 2023
"""
def f(x):
    return x  # Función de interpolación

def metodo_simpson(a, b, n):
    h = (b - a) / n
    suma = f(a) + f(b)

    for i in range(1, n, 2):
        suma += 4 * f(a + i * h)

    for i in range(2, n-1, 2):
        suma += 2 * f(a + i * h)

    return (h / 3) * suma

def metodo_romberg(a, b, n):
    R = [[0] * (n+1) for _ in range(n+1)]
    h = b - a
    R[0][0] = 0.5 * h * (f(a) + f(b))

    for i in range(1, n+1):
        h /= 2
        suma = 0
        for k in range(1, 2**i, 2):
            suma += f(a + k * h)
        R[i][0] = 0.5 * R[i-1][0] + suma * h

        for j in range(1, i+1):
            R[i][j] = R[i][j-1] + (R[i][j-1] - R[i-1][j-1]) / ((4**j) - 1)

    return R[n][n]

# Datos proporcionados
a = 0  # Límite inferior del intervalo (en minutos desde las 7:30)
b = 135  # Límite superior del intervalo (en minutos desde las 7:30)
n = 4  # Número de subdivisiones

# Aplicar el método de Simpson y el método de Romberg
area_simpson = metodo_simpson(a, b, n)
area_romberg = metodo_romberg(a, b, n)

print(f"El área aproximada usando el método de Simpson es: {area_simpson} autos*minutos")
print(f"El área aproximada usando el método de Romberg es: {area_romberg} autos*minutos")
