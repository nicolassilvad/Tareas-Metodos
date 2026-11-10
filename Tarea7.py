#Tarea 7.3 Nicolás Silva
import numpy as np
import matplotlib.pyplot as plt
np.random.seed(42)
def p(x):
    return np.sin(x)+np.random.normal(0,1e-5,len(x))
def simpson(f,a,b,n):
    h=(b-a)/n
    x=np.linspace(a,b,n+1)
    fx=f(x)
    return (h/3)*(fx[0]+2*sum(fx[2:n-1:2])+4*sum(fx[1:n:2])+fx[n]) #formula de simpson compuesto con n par
integral_exacta=1-np.cos(1) #valor exacto de la integral

valor_n=2**np.arange(1,21) #prueba valores pares de n
valor_h=1/valor_n
error=np.zeros(len(valor_n)) #error para el valor de n
for i in range(len(valor_n)):
    aprox=simpson(p,0,1,valor_n[i])
    error[i]= np.abs(aprox-integral_exacta)
#grafico
plt.loglog(valor_h,error,label='error simpson')
plt.loglog(valor_h,np.full(len(valor_h),1e-7), label='precision de $10^{-7}$')
plt.xlabel('h')
plt.ylabel('error')
plt.legend()
plt.show()

#se puede lograr una precision de 10^{-7} con n muy grandes o h muy pequeños, el error  de n es aleatorio y de media 0 enotnces 
#los errores en varios puntos se cancelan y por eso con h peuqeño  baja de 10^{-7}