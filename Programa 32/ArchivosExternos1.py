from io import open #Importa el metodo open del modulo io

Archivo_texto=open("archivo.txt", "w") #Con esto se crea el archivo y se abre (creacion y apertura)

frase="Estupendo dia para estudiar python\n el martes 7 de abril del 2020"

Archivo_texto.write(frase) #Con esto se escribe la variable en el archivo de texto (manipulacion)

Archivo_texto.close() #Con sto se cierra el archivo 


Archivo_texto=open("archivo.txt", "r") #Con esto se abre el archivo en modo lectura

texto=Archivo_texto.read()  #Con esto se lee la informacion amacenada en el archivo

Archivo_texto.close()

print(texto)


Archivo_texto=open("archivo.txt", "r")
lineas_texto=Archivo_texto.readlines()   #Con esto lee la informacion linea a linea y la guarda en una lista
Archivo_texto.close()
print(lineas_texto[0])

Archivo_texto=open("archivo.txt", "a")  #El paramatero a es append, con esto se abre el archivo en modo agregar
Archivo_texto.write("\n siempre es buena ocasion para estudiar python")
Archivo_texto.close()