#Uso de la instruccion continue
nombre="Pildoras Informaticas"
contador=0

for i in nombre:
    if i==" ":
        continue
    contador+=1 #Esto es equivalente a poner contador=contador+1

print(contador)