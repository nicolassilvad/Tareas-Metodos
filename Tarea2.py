#Tarea 2.5
#Nicolás Silva
import numpy as np
#coeficientes del polinomio de prueba
a =1
b= 9
c= 6
#calcular el discriminante
d=np.sqrt(b**2 - 4*a*c)
#calcular raices
r_1=(-b+d)/(2*a)
r_2=(-b-d)/(2*a)
#Calcular ek numero de condicionamiento bajo cambios al coeficiente b
kappa_b=np.abs(b/(2*a*r_1+b))
print("raiz 1:",r_1)
print("raiz 2:",r_2)
print("numeor de condicionamient:",kappa_b)
