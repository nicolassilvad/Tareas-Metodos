#Tarea 8.5 Nicolás Slva
import numpy as np
#datos tabal ed simulaciones
sigma=np.array([0.75,0.77,0.79,0.81,0.83])
n=np.array([1.1324e-3,1.1376e-3,1.1386e-3,1.1454e-3,1.1474e-3])
h=0.02 #paso entre datos de sigma
#formula 3 puntos
def deriv3_datos(fxo, fx2, h):
    return (fx2 - fxo)/(2*h)
derivada=deriv3_datos(n[1], n[3], h)#deriada estimada de n respecto a sigma en 0,79
print(f"derivada esimada en 0,79 con tres puntos:{derivada}")

#el error en tres puntos es (h^2)/6)*f''', con la formula de cinco puntos se puede estimar
#f''', se saca con Taylor de f(x+h) f(x-h) fx+2h) d(x-2h), si se restan los primeros dos se cancelan f'' y f
# queda 2hf'+(h^3)/3)*f''', restando los otros dos terminos queda 4hf'+(8h^3)/3)*f''', para quedarse solo con el termino con f'''
#se resta 4hf'+(h^3)/3)*f'''-2(2hf'+(h^3)/3)*f''') y queda 2h^3f''', luego se despeja f'''
#f'''=(f(x+2h)-2f(x+h)+2f(x-h)-f(x-2h)) / 2h^3
def tercera_derivada(fx,i,h):
    return(fx[i+2]-2*fx[i+1]+2*fx[i-1]-fx[i-2])/(2*h**3)
tercera_derivada_datos=tercera_derivada(n,2,h)#i=2 para sigma 0,79
error=(h**2/6)*np.abs(tercera_derivada_datos)
print(f"tercera derivada formula:{tercera_derivada_datos}")
print(f"error estimado:{error}")
ruido=1e-6
error_de_ruido=ruido/h #formula de delta/h
print(f"Eror del ruido:{error_de_ruido}")#el erro del ruido es mayor al de la formula, h fue muy  pequeño y  eso hace que
#delta/h aumente por lo tanto es encesario hacer un paso mas grande


# Nota: 7.0
# Base: 1/1; funcionamiento: 4/4; comentarios: 1/1; claridad: 1/1.
