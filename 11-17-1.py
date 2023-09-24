#!/usr/bin/env python
def gauss_seidel(t, r, c, max_iter=1000, tol=1e-100):
    for k in range(max_iter):
        t_new = (960 - 3*r - 2*c) / 4
        r_new = (510 - t_new - c) / 3
        c_new = (610 - 2*t_new - r_new) / 3

        if abs(t_new - t) < tol and abs(r_new - r) < tol and abs(c_new - c) < tol:
            return t_new, r_new, c_new

        t, r, c = t_new, r_new, c_new
        
        # Imprime el resultado de la iteración actual
        print(f"Iteración {k + 1}: t = {t}, r = {r}, c = {c}")

    raise ValueError("El método de Gauss-Seidel no convergió")

# Inicializamos las variables
t = 100
r = 100
c = 100

# Resuelve el sistema
solucion = gauss_seidel(t, r, c)
