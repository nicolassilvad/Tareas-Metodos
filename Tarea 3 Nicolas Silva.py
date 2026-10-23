#Tarea 3.1
#Nicolás Silva

import random
def prob(evento, espacio):        #funcion de probabilidad
    return len(evento & espacio)/len(espacio)
def unir (color, numeros):       #urna con 23 bolas
    return {color + numero for numero in numeros}
urna = list(unir('B', '12345678') | unir('A', '123456') | unir('R', '123456789'))
muestra = {tuple(random.choices(urna, k = 6)) for i in range(100000)}  # Monte carlo

def no_rojos(evento):                #probabilidad de que entre las tres primeras no haya ninguna roja
    s= [i[0] for i in evento[:3]]
    return s.count("R") ==0
rojo= {e for e in muestra if no_rojos(e)}
prob_rojos=prob(rojo, muestra)


def dos_de_cada_color(evento):  #sacar dos bolas de cada colo
    x= [i[0] for i in evento]
    return(x.count("B")==2
           and x.count("A")==2
           and x.count("R")==2)
colores={e for e in muestra if dos_de_cada_color(e)}
prob_colores= prob(colores,muestra)
    
print("Probabilidad de que las primeras 3 no sean roja:", prob_rojos)
print("probabilidad de que salgan dos de cada color:",prob_colores)

# Nota: 5.0
# Base: 1/1; funcionamiento: 2/4; comentarios: 1/1; claridad: 1/1.
# La simulación extrae bolas con reemplazo, pero el ejercicio exige extraer las seis bolas sin reemplazo.
