
#1.4
#Nicolás Silva
#21.376.485-3

s=0 #inicializador

for n in range (0,101):    #primera suma de 0 a 100
  for m in range (0,n+1):    #segunda suma de 0 a n
   s= s + (0.3**n)**m      #actualizar el valor de s

print(f"resultado: {s}")
