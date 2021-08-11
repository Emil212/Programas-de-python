import pickle

#lista_nombres=["Pedro", "Ana", "Maria", "Isabel"]

#Fichero_binario=open("lista_nombres", "wb") #Escritura binaria

#pickle.dump(lista_nombres, Fichero_binario) #Para colocar los elementos de la lista en el archivo

#Fichero_binario.close()

#del (Fichero_binario)

Fichero=open("lista_nombres","rb")  #Lectura binaria

lista=pickle.load(Fichero)  #Para recuperar la informacion 

print(lista)
