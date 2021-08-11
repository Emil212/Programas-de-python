from tkinter import *
from tkinter import messagebox
import sqlite3

#******************************FUNCIONES***************************************************************

def conexionBBDD():

    miconexion=sqlite3.connect("Usuarios")
    miCursor=miconexion.cursor()

    try:

        miCursor.execute('''
        CREATE TABLE DATOSUSUARIOS(ID INTEGER PRIMARY KEY AUTOINCREMENT, NOMBREUSUARIO VARCHAR(50), PASSWORD VARCHAR(50),
        APELLIDO VARCHAR(50), DIRECCION VARCHAR(50), COMENTARIOS VARCHAR(200)) ''')

        messagebox.showinfo("BBDD", "BBDD creada con exito.")

    except:
        messagebox.showwarning("¡Atencion!", "La BBDD ya existe.")

def SalirApp():
    valor=messagebox.askquestion("Salir","¿Deseas salir de la aplicación?")

    if valor=="yes":
        root.destroy()

def LimpiarCampos():

    miID.set("")
    miNombre.set("")
    miPass.set("")
    miApellido.set("")
    miDireccion.set("")
    TextoComentario.delete(1.0, END)    #Para borrar el texto del cuadro de comentarios

def Crear():
    miConexion=sqlite3.connect("Usuarios")
    miCursor=miConexion.cursor()



    """miCursor.execute("INSERT INTO DATOSUSUARIOS VALUES(NULL, '" + miNombre.get() +
    "','" + miPass.get() + 
    "','" + miApellido.get() +
    "','" + miDireccion.get() +
    "','" + TextoComentario.get("1.0", END) + "')")"""

    if miNombre.get()=='' or miPass.get()=='' or miApellido.get()=='' or miDireccion.get()=='':
        messagebox.showwarning("BBDD", "El unico campo en blanco debe ser la ID")

    elif miNombre.get().isdigit():
        messagebox.showwarning("BBDD", "El unico campo en blanco debe ser la ID")
        miNombre.set("")
    
    elif miApellido.get().isdigit():
        messagebox.showwarning("BBDD", "El apellido no puede tener digitos")
        miApellido.set("")
    
    elif miID.get().isalpha():
        messagebox.showwarning("BBDD", "El ID se asigna de manera automatica.")
        miID.set("")
        

    else:
        
        datos=miNombre.get(), miPass.get(), miApellido.get(), miDireccion.get(), TextoComentario.get("1.0", END)


        miCursor.execute("INSERT INTO DATOSUSUARIOS VALUES(NULL,?,?,?,?,?)",(datos))    
    
        miConexion.commit()

        messagebox.showinfo ("BBDD", "Registro insertado con exito.")

        LimpiarCampos()

def Leer():
    miConexion=sqlite3.connect("Usuarios")
    miCursor=miConexion.cursor()
    TextoComentario.delete(1.0, END)


    if miID.get().isdigit():


        miCursor.execute("SELECT * FROM DATOSUSUARIOS WHERE ID=" + miID.get())

        elUsuario=miCursor.fetchall()

        for Usuario in elUsuario:

            miID.set(Usuario[0])
            miNombre.set(Usuario[1])
            miPass.set(Usuario[2])
            miApellido.set(Usuario[3])
            miDireccion.set(Usuario[4])
            TextoComentario.insert(1.0, Usuario[5])
            miConexion.commit()
        
    else:

        messagebox.showwarning("BBDD", "Introduzca una ID válida")
        



def Actualizar():

#  "', PASSWORD='" + miPass.get() +
#  "', APELLIDO='" + miApellido.get() +
#  "', DIRECCION='" + miDireccion.get() +
# "', COMENTARIOS='" + TextoComentario.get("1.0",END) +
#"'WHERE ID=" + miID.get())"""

    if miID.get().isdigit():

        valor=messagebox.askquestion("Actualizar","¿Deseas actualizar el registro?")

        if valor=="yes":
        
            miConexion=sqlite3.connect("Usuarios")
            miCursor=miConexion.cursor()

            datos=miNombre.get(), miPass.get(), miApellido.get(), miDireccion.get(), TextoComentario.get("1.0", END)
            miCursor.execute("UPDATE DATOSUSUARIOS SET NOMBREUSUARIO=?, PASSWORD=?, APELLIDO=?, DIRECCION=?, COMENTARIOS=? " + 
            "WHERE ID=" + miID.get(), (datos))

            miConexion.commit()
            messagebox.showinfo("BBDD", "Registro actualizado con exito.")
            LimpiarCampos()
    
    else:
        messagebox.showwarning("BBDD", "Introduzca una ID válida")



def Eliminar():

    
    valor=messagebox.askquestion("Eliminar","¿Deseas eliminar el registro?")

    if valor=="yes":
        
        miConexion=sqlite3.connect("Usuarios")
        miCursor=miConexion.cursor()

        miCursor.execute("DELETE FROM DATOSUSUARIOS WHERE ID=" + miID.get())
        miConexion.commit()
        messagebox.showinfo("BBDD", "Se ha eliminado el registro con exito.")

        LimpiarCampos()

def Verificar():

    miConexion=sqlite3.connect("Usuarios")
    miCursor=miConexion.cursor()
    #miCursor.execute("SELECT * FROM DATOSUSUARIOS WHERE EXISTS (SELECT 1 FROM  DATOSUSUARIOS WHERE ID='" + miNombre.get() + "')")












#*********************************EMPIEZA LA CONFIGURACION DE LA INTERFAZ****************************************************

root=Tk()
root.resizable(0,0)

barraMenu=Menu(root)
root.config(menu=barraMenu, width=300, height=300)

bbddMenu=Menu(barraMenu, tearoff=0)
bbddMenu.add_command(label="Conectar", command=conexionBBDD)
bbddMenu.add_command(label="Salir", command=SalirApp)

borrarMenu=Menu(barraMenu, tearoff=0)
borrarMenu.add_command(label="Borrar campos", command=LimpiarCampos)

crudMenu=Menu(barraMenu, tearoff=0)
crudMenu.add_command(label="Crear", command=Crear)
crudMenu.add_command(label="Leer", command=Leer)
crudMenu.add_command(label="Actualizar", command=Actualizar)
crudMenu.add_command(label="Borrar", command=Eliminar)

ayudaMenu=Menu(barraMenu, tearoff=0)
ayudaMenu.add_command(label="Licencia")
ayudaMenu.add_command(label="Acerca de...")

barraMenu.add_cascade(label="BBDD", menu=bbddMenu)
barraMenu.add_cascade(label="Borrar", menu=borrarMenu)
barraMenu.add_cascade(label="CRUD", menu=crudMenu)
barraMenu.add_cascade(label="Ayuda", menu=ayudaMenu)

#-----------------------------COMIENZO DE CAMPOS***************************************************************************************

miFrame=Frame(root)
miFrame.pack()

miID=StringVar()    #Para rescatar la informacion indicando que va a haber una cadena de caracteres 
miNombre=StringVar()
miApellido=StringVar()
miPass=StringVar()
miDireccion=StringVar()


cuadroID=Entry(miFrame, textvariable=miID)
cuadroID.grid(row=0, column=1, padx=10, pady=10)


cuadroNombre=Entry(miFrame,textvariable=miNombre)
cuadroNombre.grid(row=1, column=1, padx=10, pady=10)
cuadroNombre.config(fg="red", justify="right")

cuadroPass=Entry(miFrame, textvariable=miPass)
cuadroPass.grid(row=2, column=1, padx=10, pady=10)
cuadroPass.config(show="*")

cuadroApellido=Entry(miFrame, textvariable=miApellido)
cuadroApellido.grid(row=3, column=1, padx=10, pady=10)

cuadroDireccion=Entry(miFrame, textvariable=miDireccion)
cuadroDireccion.grid(row=4, column=1, padx=10, pady=10)

TextoComentario=Text(miFrame, width=16, height=5)
TextoComentario.grid(row=5, column=1, padx=10, pady=10)

scrollvert=Scrollbar(miFrame, command=TextoComentario.yview)
scrollvert.grid(row=5, column=2, padx=10, sticky="nsew")

TextoComentario.config(yscrollcommand=scrollvert.set)


#****************************************Aqui comienzan las etiquetas************************************************

idLabel=Label(miFrame, text="ID: ")
idLabel.grid(row=0, column=0, sticky="e", padx=10, pady=10)

nombreLabel=Label(miFrame, text="Nombre: ")
nombreLabel.grid(row=1, column=0, sticky="e", padx=10, pady=10)

passLabel=Label(miFrame, text="Password: ")
passLabel.grid(row=2, column=0, sticky="e", padx=10, pady=10)

apellidoLabel=Label(miFrame, text="Apellido: ")
apellidoLabel.grid(row=3, column=0, sticky="e", padx=10, pady=10)

direccionLabel=Label(miFrame, text="Direccion: ")
direccionLabel.grid(row=4, column=0, sticky="e", padx=10, pady=10)

comentariosLabel=Label(miFrame, text="Comentarios: ")
comentariosLabel.grid(row=5, column=0, sticky="e", padx=10, pady=10)

#***************************Aqui los botones*****************************************

miFrame2=Frame(root)
miFrame2.pack()

botonCrear=Button(miFrame2, text="Crear", command=Crear)
botonCrear.grid(row=1, column=0, sticky="e", padx=10, pady=10)

botonLeer=Button(miFrame2, text="Leer", command=Leer)
botonLeer.grid(row=1, column=1, sticky="e", padx=10, pady=10)

botonActualizar=Button(miFrame2, text="Actualizar", command=Actualizar)
botonActualizar.grid(row=1, column=2, sticky="e", padx=10, pady=10)

botonBorrar=Button(miFrame2, text="Borrar", command=Eliminar)
botonBorrar.grid(row=1, column=3, sticky="e", padx=10, pady=10)


root.mainloop()
