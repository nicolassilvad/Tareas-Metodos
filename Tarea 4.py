#Tarea 4.3
#Nicolás Silva

import numpy as np
from scipy.special import factorial
lamda=2.0
#1 funcion caracteristica
def rho_ñ(k,lamda):
    return lamda/(lamda+1j*k) #calculo de rho

print("1. Calcule la función característica:",rho_ñ(1,lamda))#con k=1
#2 cumulantes
def cumulantes(n,lamda):
    return factorial(n-1)/lamda**n
print ("2.Calcule los primeros cuatro cumulantes de esta distribución:")#print el valor exacto y simulado
for n in range(1,5):
    print(n,cumulantes(n,lamda))
#3 comparar con la gaussiana
cumulantes_gaussiana=[cumulantes(1,lamda),cumulantes(2,lamda),0,0]
print("3.Basado en el punto anterior, compare con la distribución gaussiana:")
for n in range (1,5):
    print(n,cumulantes(n,lamda),cumulantes_gaussiana[n-1])

# Nota: 7.0
# Base: 1/1; funcionamiento: 4/4; comentarios: 1/1; claridad: 1/1.
