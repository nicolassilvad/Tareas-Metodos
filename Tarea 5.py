#tarea 5.6 Nicolas Silva
import math
import numpy as np

lista = [2,4,6]
for n in lista:
    determinante=math.factorial(n)
    matriz_adjunta=math.factorial(n-1)*(n**2)
    operaciones= determinante+matriz_adjunta
    print(f" resultados para matriz 2 , 4, y 6 respectivamente")
    print(f"1.- numero de operaciones:n!={determinante}")
    print(f"2.-numero de operaciones: {matriz_adjunta}")
    print(f"3.- Para n grandes crecce de forma factorial con n*n!, total operaciones:{operaciones}")
print("la expansion por cofactores en una matriz n*n se abre en determinantes de (n-1)-(n-1) que se siguen abriendo (n-1) veces haciendo que haga n! operaciones")

# Nota: 6.0
# Base: 1/1; funcionamiento: 4/4; comentarios: 0/1; claridad: 1/1.
# Faltan comentarios que expliquen el cálculo del costo del determinante, la adjunta y la suma de ambas contribuciones.
