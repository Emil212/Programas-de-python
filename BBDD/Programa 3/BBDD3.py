import sqlite3 

miConexion=sqlite3.connect("GestorProductos")

miCursor=miConexion.cursor()

#miCursor.execute("SELECT * FROM PRODUCTOS WHERE SECCION='confeccion'")  #Para ver los productos

miCursor.execute("UPDATE PRODUCTOS SET PRECIO=35 WHERE NOMBRE_PRODUCTO='pelota'")

miCursor.execute("DELETE FROM PRODUCTOS WHERE ID=5")

productos=miCursor.fetchall()

print(productos)

miConexion.commit()
miConexion.close()