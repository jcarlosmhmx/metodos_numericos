#!/usr/bin/env python
"""
Este módulo Plantea el sistema de ecuaciones para el caso planteado y resuélvelo aplicando los métodos Simpson y Romberg 
encuentra la solución programando cada método. (Ver página 647, ejercicio 21.23) 
Author: Equipo 8 Métodos Numéricos
Fecha: Octubre 8, 2023
"""
def metodo_simpson(datos):
    h = datos[1][0] - datos[0][0]
    n = len(datos)
    suma = datos[0][1] + datos[n-1][1]

    for i in range(1, n-1):
        coef = 4 if i % 2 != 0 else 2
        suma += coef * datos[i][1]

        print(f"Iteración {i}:")
        print(f"  Coeficiente: {coef}")
        print(f"  Valor de y({datos[i][0]}): {datos[i][1]}\n")

    return (h / 3) * suma

def metodo_romberg(datos):
    n = len(datos)Y
    R = [[0] * n for _ in range(n)]
    R[0][0] = (datos[n-1][0] - datos[0][0]) * (datos[0][1] + datos[n-1][1]) / 2

    for i in range(1, n):
        sumatoria = sum(datos[j][1] for j in range(1, n-1, 2))
        R[i][0] = 0.5 * R[i-1][0] + (datos[n-1][0] - datos[0][0]) * sumatoria / n

        print(f"Iteración {i}:")
        print(f"  Valor de R({i},{0}): {R[i][0]}\n")

        for j in range(1, i+1):
            R[i][j] = R[i][j-1] + (R[i][j-1] - R[i-1][j-1]) / (4**j - 1)

            print(f"  Valor de R({i},{j}): {R[i][j]}\n")

    return R[n-1][n-1]

# Datos proporcionados (tiempo en minutos desde las 7:30)
datos = [
    (0, 18),
    (15, 24),
    (30, 14),
    (45, 24),
    (75, 21),
    (135, 9)
]

# Aplicar los métodos de Simpson y Romberg
area_simpson = metodo_simpson(datos)
area_romberg = metodo_romberg(datos)

print(f"El número aproximado de autos que pasaron entre las 7:30 y las 9:15 usando el método de Simpson es: {area_simpson} autos")
print(f"El número aproximado de autos que pasaron entre las 7:30 y las 9:15 usando el método de Romberg es: {area_romberg} autos")
