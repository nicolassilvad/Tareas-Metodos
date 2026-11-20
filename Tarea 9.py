#Tarea 9.9 Nicolás Silva
import numpy as np
def rk4_step(f, fi, t, w, h): #codigo de la clase pero el corrector itera p veces
    
    k1 = h*fi
    k2 = h*f(t+h/2, w+k1/2)
    k3 = h*f(t+h/2, w+k2/2)
    k4 = h*f(t + h, w + k3)
    return (k1 + 2*k2 + 2*k3 + k4)/6
    
def apc4(f, a, b, yo, N,p):
    
    h = (b-a)/N
    i = 0
    w = yo
    t = a
    
    ws = np.zeros(N+1)
    ts = np.zeros(N+1)
    fi = 0
    fim1 = 0
    fim2 = 0
    fim3 = 0
    
    for i in range(N):
        ts[i] = t
        ws[i] = w
        fim3 = fim2
        fim2 = fim1
        fim1 = fi
        fi = f(t,w)
        if i < 3:
            w += rk4_step(f, fi, t, w, h)
        else:
            w = ws[i] + h*(55*fi - 59*fim1 +37*fim2 - 9*fim3)/24
            for j in range(p):
                w = ws[i] + h*(9*f(t+h, w) + 19*fi - 5*fim1 + fim2)/24
        t += h
    ws[N] = w
    ts[N] = t 
    return ts, ws
def f(t,y):
    return y/t-(y/t)**2 #problema valor inicial
a=1 
b=2 
yo=1
def solucion_analitica(t):
    return t/(1+np.log(t))
for p in [2,3,4]:            
    solucion=apc4(f, a, b, yo, 10,p) #h=0.1 es lo mismo que N=10
    error=np.abs(solucion[1]-solucion_analitica(solucion[0]))
    print(f"p={p}:error={max(error)}") #los tres valores de p dan casi el mismo error pero en p=2 da un resultado mejor
    