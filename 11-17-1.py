#!/usr/bin/env python
"""
Este módulo utiliza el método numérico Guess Seidel para reolver la ecuación descrita.
Author: Equipo 8 Métodos Numéricos
Date: September 24, 2023
"""
def gauss_seidel(A, b, x0=None, tol=1e-10, max_iter=1000):
    n = len(b)
    x = x0 or [0.0] * n

    for k in range(max_iter):
        x_new = x.copy()
        for i in range(n):
            s1 = sum(A[i][j] * x_new[j] for j in range(i))
            s2 = sum(A[i][j] * x[j] for j in range(i + 1, n))
            x_new[i] = (b[i] - s1 - s2) / A[i][i]

        if all(abs(x_new[i] - x[i]) < tol for i in range(n)):
            return x_new

        x = x_new
        
        # Imprime el resultado de la iteración actual
        print(f"Iteración {k + 1}: t = {x[0]}, r = {x[1]}, c = {x[2]}")

    raise ValueError("El método de Gauss-Seidel no convergió")

# Coeficientes de las ecuaciones
A = [[4, 3, 2],
     [1, 3, 1],
     [2, 1, 3]]

# Términos independientes
b = [960, 510, 610]

# Resuelve el sistema
solucion = gauss_seidel(A, b)
