#!/usr/bin/env python
"""
Este módulo utiliza el método numérico Jacobi para reolver la ecuación descrita.
Author: Equipo 8 Métodos Numéricos
Date: September 24, 2023
"""
def jacobi(A, b, x0=None, max_iter=1000, tol=1e-10):
    n = len(b)
    x = x0 or [0.0] * n

    D = [A[i][i] for i in range(n)]
    R = [[A[i][j] if i != j else 0 for j in range(n)] for i in range(n)]

    for k in range(max_iter):
        x_new = [(b[i] - sum(R[i][j] * x[j] for j in range(n))) / D[i] for i in range(n)]

        if all(abs(x_new[i] - x[i]) < tol for i in range(n)):
            return x_new

        x = x_new
        
        # Imprime el resultado de la iteración actual
        print(f"Iteración {k + 1}: t = {x[0]}, r = {x[1]}, c = {x[2]}")

    raise ValueError("El método de Jacobi no convergió")

# Coeficientes de las ecuaciones
A = [[4, 3, 2],
     [1, 3, 1],
     [2, 1, 3]]

# Términos independientes
b = [960, 510, 610]

# Resuelve el sistema
solucion = jacobi(A, b)

# Imprime la solución
print(f"x = {solucion[0]}, y = {solucion[1]}, z = {solucion[2]}")
