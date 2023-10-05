#!/usr/bin/env python
"""
Para la integración de ecuaciones, utiliza el método de integración de Romberg. 
Adicional al criterio del 1% especificado, realiza tu programa modificando el criterio de detención del 1% solicitado 
y realiza el programa con los criterios de detención al 0.5% y al 1.5% (Ver página 667, ejercicio 22.15) 
Author: Equipo 8 Métodos Numéricos
Fecha: Octubre 8, 2023
"""
# Definimos la función H(x)
def H(x):
    valores = [0, 1.9, 2, 2, 2.4, 2.6, 2.25, 1.12, 0]
    return valores[int(x/2)]

# Implementamos el método de Romberg con impresión de iteraciones
def romberg(a, b, n):
    R = [[0] * (n+1) for _ in range(n+1)]
    h = (b - a)

    R[0][0] = 0.5 * h * (H(a) + H(b))

    for i in range(1, n+1):
        h /= 2
        suma = sum(H(a + k * h) for k in range(1, 2**i, 2))
        R[i][0] = 0.5 * R[i-1][0] + suma * h

        print(f"Iteración {i}:")
        print(f"  R({i},0): {R[i][0]}")

        for j in range(1, i+1):
            R[i][j] = R[i][j-1] + (R[i][j-1] - R[i-1][j-1]) / ((4**j) - 1)

            print(f"  R({i},{j}): {R[i][j]}")

    return R[n][n]

# Llamamos a la función Romberg para calcular la integral e imprimir las iteraciones
resultado = romberg(0, 16, 4)

print(f"\nEl área de la sección transversal del río es aproximadamente: {resultado} unidades cuadradas.")
