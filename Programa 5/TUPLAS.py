MiTupla=("Juan", 13, 1, 1995)  #Las tuplas llevan parentesis o no parentesis y las listas corchetes, si no se ponen los parentesis se dice empaquetado de tupla
MiLista=list(MiTupla) #Convierte la tupla en una lista mediante el metodo list
MiLista2=("Emiliano", 25, 1, 1999)
MiTupla2=tuple(MiLista2) #Convierte la lista en una tupla mediante el metodo tuple
print(MiTupla2)
print("Juan" in MiTupla)  #verifica si un elemnto esta dentro de una tupla
print(MiTupla.count(13)) #Imprime cuantas veces se encuentra un elemento en una tupla
print(len(MiTupla))  #Imprime la longitud de la tupla
MiTupla3=("Juan",) #Crea una tupla unitaria
print(len(MiTupla3))
MiTupla4=("Juan", 13, 1, 1995)
nombre, dia, mes, year = MiTupla4 #Desempaquetado de tupla, de esta forma se asignan los elementos de una tupla en diferentes variables
print(nombre)
print(dia)
print(mes)
print(year)

#Las tuplas no se pueden modificar


