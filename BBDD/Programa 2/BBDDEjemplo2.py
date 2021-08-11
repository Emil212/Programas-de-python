import sqlite3

miConexion=sqlite3.connect("GestorProductos")

miCursor=miConexion.cursor()

#Para crear el campo clave, no se pude repetir la informacion de un campo clave 

""" miCursor.execute('''
    CREATE TABLE PRODUCTOS (
    CODIGO_ARTICULO VARCHAR(4) PRIMARY KEY,
    NOMBRE_PRODUCTO VARCHAR(50),
    PRECIO INTEGER,
    SECCIOM VARCHAR(20))

''') 

productos=[
    ("AR01", "pelota", 20, "jugueteria"),
    ("AR02", "pantalon", 10, "confeccion"),
    ("AR03", "destornillador", 25, "ferreteria"),
    ("AR04", "jarron", 40, "ceramica")

] """

miCursor.execute('''
    CREATE TABLE PRODUCTOS (
    ID INTEGER PRIMARY KEY AUTOINCREMENT,
    NOMBRE_PRODUCTO VARCHAR(50) UNIQUE,     
    PRECIO INTEGER,
    SECCION VARCHAR(20))

''')

productos=[
    ("pelota", 20, "jugueteria"),
    ("pantalon", 10, "confeccion"),
    ("destornillador", 25, "ferreteria"),
    ("jarron", 40, "ceramica"),
    ("pantalones", 20, "confeccion")

]

miCursor.executemany("INSERT INTO PRODUCTOS VALUES (NULL,?,?,?)", productos)

#miCursor.execute("INSERT INTO PRODUCTOS VALUES ('AR06', 'tren', 15, 'jugueteria')")

miConexion.commit()
miConexion.close()