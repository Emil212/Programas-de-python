from io import open

Archivo_texto=open("archivo.txt", "r+") #Con esto se crea el archivo y se abre (creacion y apertura) Lectura y escritura

#print(Archivo_texto.read(11)) #Hace un lectura hasta donde se posiciona el puntero

#print(Archivo_texto.read()) #Se empieza a imprimir desde la posicion donde se quedo el puntero
#Cuando lee el archivo recorre todo desde el principio hasta el final, el puntero por defecto se coloca en la ultima posicion despues de leer

#Archivo_texto.seek(0)   #Con esta instruccion el puntero se puede clocar en una posicion en especifico 

#print(Archivo_texto.read())

#Archivo_texto.seek(len(Archivo_texto.read())/2)
#print(Archivo_texto.readlines())

lista_texto=Archivo_texto.readlines()

lista_texto[1]="Esta linea ha sido incluida desde el exterior\n"

Archivo_texto.seek(0)

Archivo_texto.writelines(lista_texto)

Archivo_texto.close()
