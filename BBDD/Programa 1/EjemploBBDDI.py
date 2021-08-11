import sqlite3  

miConexion=sqlite3.connect("PrimeraBase")  #Crear la conexion

miCursor=miConexion.cursor()    #Crear el cursor o puntero

#miCursor.execute("CREATE TABLE PRODUCTOS (NOMBRE_ARTICULO VARCHAR (50), PRECIO INTEGER, SECCION VARCHAR (20))")

#miCursor.execute("INSERT INTO PRODUCTOS VALUES('BALON', 15, 'DEPORTES')") #para insertar informacion en la tabla


#variosProductos= [ 

 #   ("Camiseta", 10, "Deportes"),
  #  ("Jarron", 30, "ceramica"),
   # ("Camion", 20, "Juguereteria")

#]

#miCursor.executemany("INSERT INTO PRODUCTOS VALUES (?,?,?)", variosProductos)    #Insertar lantos ? como campos 

miCursor.execute("SELECT * FROM PRODUCTOS") #Para recuperar la informacion de la BBDD

variosProductos=miCursor.fetchall() #Para mostrar la informacion

for producto in variosProductos:
    print("Nombre articulo:",producto[0], "Seccion:", producto[1])

miConexion.commit() #Se confirman los cambios en la tabla para insertar un registro


miConexion.close()  #Para cerrar la base de datos
