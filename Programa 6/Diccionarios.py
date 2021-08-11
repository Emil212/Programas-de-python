MiDiccionario={"Alemaria":"Berlin", "Francia":"Paris", "Reino Unido" : "Londres", "España":"Madrid"} #Los diccionarios llevan llaves y son de tipo clave:valor
MiDiccionario["Italia"] = "Lisboa" #Agrega un nuevo elemento al diccionario hasta el final
print(MiDiccionario["España"]) #Se pone la clave y nos arroja el valor correspondiente
print(MiDiccionario)
MiDiccionario["Italia"] = "Roma" #Corrije el dato del diccionario ya que se sobreescribe el anterior
print(MiDiccionario)
del MiDiccionario["Reino Unido"]#Sirve para eliminar un elemento del diccionario introduciendo la clave
print(MiDiccionario)

MiDiccionario2= {"Alemania":"Berlin", 23:"Jordan", "Mosqueteros":3} #El diccionario puede tener elementos de diferentes tipos 
print(MiDiccionario2)

MiTupla=("España","Francia","Reino Unido", "Alemania")
MiDiccionario3={MiTupla[0]:"Madrid", MiTupla[1]:"Paris", MiTupla[2]:"Londres", MiTupla[3]:"Berlin"} #Se asignas los valores a las claves
print(MiDiccionario)
print(MiDiccionario3["Francia"])  #Para imprimir una clave en especifico se pone el valor

MiDiccionario4={23:"Jordan", "Nombre":"Michael", "Equipo":"Chicago", "anillos":{"Temporadas":[1991,1992,1993,1996,1997,1998]}} #Se pueden asinar mas de un valor a una clave usando tuplas o guardando un diccionario dentro de otro
print(MiDiccionario4["anillos"]) #diccionario dentro de otro diccionario dentro de una tupla

print(MiDiccionario4.keys()) #Imprime las claves de un diccionario

print(MiDiccionario4.values()) #Imprime los valores de un diccionario

print(len(MiDiccionario)) #Imprime la longitud de claves y valores 
 
