from tkinter import *
from tkinter import messagebox

root=Tk()

def infoAdicional():
    messagebox.showinfo("Procesador de emiliano", "procesador de textos version 2020")

def avisoLicencia():
    messagebox.showwarning("Licencia", "Producto bajolicencia GNU")

def salirAplicacion():
    #valor=messagebox.askquestion("Salir", "¿Deseas salir de la aplicacion?")
    valor=messagebox.askokcancel("Salir", "¿Deseas salir de la aplicacion?")

    if valor==True:
        root.destroy()  #Para salir de la aplicacion 

def cerrarDoc():
    valor1=messagebox.askretrycancel("Reintentar", "No es posible cerrar . Documento bloqueado")
        
    if valor1==False:
        root.destroy()


BarraMenu=Menu(root)
root.config(menu=BarraMenu, width=300, height=300)


archivoMenu=Menu(BarraMenu, tearoff=0)

archivoMenu.add_command(label="Nuevo")
archivoMenu.add_command(label="Guardar")
archivoMenu.add_command(label="Guardar como")
archivoMenu.add_separator()
archivoMenu.add_command(label="Cerrar", command=cerrarDoc)
archivoMenu.add_command(label="Salir", command=salirAplicacion)



archivoEdicion=Menu(BarraMenu, tearoff=0)

archivoEdicion.add_command(label="Copiar")
archivoEdicion.add_command(label="Cortar")
archivoEdicion.add_command(label="Pegar")




archivoHerramientas=Menu(BarraMenu, tearoff=0)


archivoAyuda=Menu(BarraMenu, tearoff=0)

archivoAyuda.add_command(label="Licencia", command=avisoLicencia)
archivoAyuda.add_command(label="Acerca de...", command=infoAdicional)


BarraMenu.add_cascade(label="Archivo", menu=archivoMenu)
BarraMenu.add_cascade(label="Edicion", menu=archivoEdicion)
BarraMenu.add_cascade(label="Herramientas", menu=archivoHerramientas)
BarraMenu.add_cascade(label="Ayuda", menu=archivoAyuda)
root.mainloop()