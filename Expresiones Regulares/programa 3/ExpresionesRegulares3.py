import re

ListaNombres=['Ana', 'Pedro', 'Mario', 'Rosa', 'Sandra', 'Celia']

for elemento in ListaNombres:
    if re.findall('[o-t]', elemento):   #Nombres que dentro tienen desde la o hasta la t, distingue entre mayusculas y minusculas
        print(elemento)

#Se pueden mezclar con los otros metacaracteres vistos en el video anterior

ListaCiudades=['Ma1', 'Ma2', 'Ma3','Ma4', 'Se1', 'Se2', 'Se3' ]

for elemento in ListaCiudades:
    if re.findall('Ma[^0-3]', elemento): #El ^ se pone alt+94, de3 esta forma se niega el rango y muestra lo que esta fuera
        print(elemento)

for elemento in ListaCiudades:
    if re.findall('Ma[0-3A-B]', elemento):
        print(elemento)

for elemento in ListaCiudades:
    if re.findall('Ma[.:]', elemento):  #Selecciona los que tengan .:
        print(elemento)
   