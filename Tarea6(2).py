#Tarea 6.10 Nioclas SIlva
import numpy as np

# copie las funciones de la clase para la tarea
#..................................................
def find_ind(x, puntos):
    for i in range(len(puntos)):
        if x < puntos[i,0] and i != 0:
            return i-1                         

def spline_coefs(puntos):

    n = len(puntos) - 1

    h = np.zeros(n)
    for i in range(n):
        h[i] = puntos[i + 1][0] - puntos[i][0]  

    a = puntos[:,1]
    alpha = np.zeros(n - 1)
    for i in range(1, n):
        alpha[i-1] = (3/h[i])*(a[i+1] - a[i]) - (3/h[i-1])*(a[i] - a[i-1])

    l = np.ones(n + 1)
    mu = np.zeros(n)
    z = np.zeros(n + 1)
    for i in range(1, n):
        l[i] = 2*(puntos[i+1][0] - puntos[i-1][0]) - h[i-1]*mu[i-1]
        mu[i] = h[i]/l[i]
        z[i] = (alpha[i-1] - h[i-1]*z[i-1])/l[i]
    b = np.zeros(n)
    c = np.zeros(n+1)
    d = np.zeros(n)
    for j in range(n-1,-1,-1):
        c[j] = z[j] - mu[j]*c[j+1]
        b[j] = (a[j+1] - a[j])/h[j] - h[j]*(c[j+1] + 2*c[j])/3
        d[j] = (c[j+1] - c[j])/(3*h[j])

    return a, b, c, d                          

def spline_eval(x, coefs, puntos):

    if x >= puntos[-1,0]:
        return puntos[-1,1]
    elif x <= puntos[0,0]:
        return puntos[0,1]

    i = find_ind(x, puntos)
    a, b, c, d = coefs
    return (a[i] + b[i]*(x - puntos[i][0]) + \
            c[i]*(x - puntos[i][0])**2 + d[i]*(x - puntos[i][0])**3)   
#.............................................................................
#funcion de la tarea 6.10
import numpy as np

def f(x):
    return 4*x**3 - 3*x**2 + x - 5
x = np.linspace(-1, 1, 5)    # puntos donde comparo
xp = np.array([-1, 1])
puntos = np.array([[xi, f(xi)] for xi in xp])
coefs = spline_coefs(puntos)
print(" spline en x=-1 y x=1 puntos")
print("con c y d 0):", coefs[2][0], coefs[3][0])
for xi in x:
    s = spline_eval(xi, coefs, puntos)
    print("x =", xi, " f(x) =", round(f(xi), 4), "spline =", round(s, 4))

# la spline cubica es differente al polinomio original porque la primera
#tiene como consdicion que la segunda derivada sea 0 en los extremos y la funcion f(X) no lo cumpl.

#splines por intervalos con 4 puntos equidistantes
xp = np.linspace(-1, 1, 4)
puntos = np.array([[xi, f(xi)] for xi in xp])
coefs = spline_coefs(puntos)
print()
print("spline con 4 puntos")
for xi in x:
    s = spline_eval(xi, coefs, puntos)
    print("x =", xi, "f(x) =", round(f(xi), 4), "spline =", round(s, 4)) #con los 4 puuntos queda una mejor aproximacion