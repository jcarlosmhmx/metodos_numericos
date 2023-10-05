#!/usr/bin/env python
"""
Este módulo Plantea el sistema de ecuaciones para el caso planteado y resuélvelo aplicando la regla de trapecio 
encuentra la solución programando cada método. (Ver página 647, ejercicio 21.23) 
Author: Equipo 8 Métodos Numéricos
Fecha: Octubre 8, 2023
"""
def regla_trapecio(tiempo, autos):
    area = 0
    for i in range(len(tiempo) - 1):
        base = tiempo[i+1] - tiempo[i]
        altura_promedio = (autos[i] + autos[i+1]) / 2
        area += base * altura_promedio
        
        print(f"Iteración {i+1}:")
        print(f"  Base: {base} minutos")
        print(f"  Altura promedio: {altura_promedio} autos")
        print(f"  Área parcial: {base * altura_promedio} autos*minutos")
        print(f"  Área acumulada: {area} autos*minutos\n")
    return area

# Datos proporcionados
tiempo = [0, 15, 30, 45, 75, 135]  # Tiempo en minutos desde las 7:30
autos = [18, 24, 14, 24, 21, 9]    # Número de autos

# Aplicar la regla del trapecio
area_aproximada = regla_trapecio(tiempo, autos)

print(f"El número aproximado de autos que pasaron entre las 7:30 y las 9:15 es: {area_aproximada}")
