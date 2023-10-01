#!/usr/bin/env python
"""
Este módulo utiliza el método numérico Gauss Seidel para reolver la ecuación descrita.
Author: Equipo 8 Métodos Numéricos
Fecha: Septiembre 28, 2023
"""
def gauss_seidel_iteration(A, b, t0=None, r0=None, c0=None, tol=1e-10, max_iter=1000):
    n = len(b)
    t0 = t0 or 0
    r0 = r0 or 0
    c0 = c0 or 0
    
    t, r, c = t0, r0, c0
    
    for k in range(max_iter):
        t_old, r_old, c_old = t, r, c
        
        # Actualizar t
        t = (b[0] - A[0][1]*r - A[0][2]*c) / A[0][0]
        
        # Actualizar r
        r = (b[1] - A[1][0]*t - A[1][2]*c) / A[1][1]
        
        # Actualizar c
        c = (b[2] - A[2][0]*t - A[2][1]*r) / A[2][2]
        
        # Mostrar los resultados de la iteración actual
        print(f"Iteración {k+1}: t = {t}, r = {r}, c = {c}")
        
        # Comprobar convergencia
        if abs(t - t_old) < tol and abs(r - r_old) < tol and abs(c - c_old) < tol:
            break
    
    return t, r, c

# Definir la matriz de coeficientes y el vector de términos independientes
A = [[4, 3, 2], [1, 3, 1], [2, 1, 3]]
b = [960, 510, 360]

# Llamada a la función
result_t, result_r, result_c = gauss_seidel_iteration(A, b)

# Imprimir el resultado final
print("\nResultado final:")
print(f"t = {result_t}")
print(f"r = {result_r}")
print(f"c = {result_c}")
