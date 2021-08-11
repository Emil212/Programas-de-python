MiLista=["Maria","Pepe", "Martha", "Antonio"] #Pueden almacenar diferentes tipos de datos

MiLista2=["Ximena", "Mike"]

#Si se agrega * eb la declaracion de la lista se repiten los elementos de la lista

MiLista3=MiLista+MiLista2 #Se pueden sumar dos listas, los elemtos de lasegunda lista se agregan al final

MiLista.append("Sandra") #Para agregar al final de la lista

MiLista.insert(2,"Ariel") #Para agregar en una posicion especifica

MiLista.extend(["Ana", "Lucia"]) #Agrega mas de un elemento al final de la lista

MiLista.remove("Ana") #Para eliminar un elemto en una lista

MiLista.pop() #Para eliminar el ultimo elemnto de una lista 

print(MiLista[:]) #Python puede trabajar con indices negativos

print(MiLista.index("Antonio"))  #Imprime el indice  en caso de haber mas de dos elementos iiguales manda el indice del primer elemento

print("Pepe" in MiLista) #Para ver si un elemento se encuentra en una lista

print(MiLista2[:])

print(MiLista3[:])



