from tkinter import *

raiz=Tk()

MiFrame=Frame(raiz, width=1200, height=600)
MiFrame.pack()

CuadroNombre=Entry(MiFrame)
CuadroNombre.grid(row=0, column=1, padx=10, pady=10)
CuadroNombre.config(fg="red", justify="center")

CuadroPass=Entry(MiFrame)
CuadroPass.grid(row=1, column=1, padx=10, pady=10)
CuadroPass.config(show="*")

CuadroApellido=Entry(MiFrame)
CuadroApellido.grid(row=2, column=1, padx=10, pady=10)

CuadroDireccion=Entry(MiFrame)
CuadroDireccion.grid(row=3, column=1, padx=10, pady=10)


nombreLabel=Label(MiFrame, text="Nombre: ")
nombreLabel.grid(row=0, column=0, sticky="e", padx=10, pady=10)

passLabel=Label(MiFrame, text="Pasword: ")
passLabel.grid(row=1, column=0, sticky="e", padx=10, pady=10)

apellidoLabel=Label(MiFrame, text="Apelldo: ")
apellidoLabel.grid(row=2, column=0, sticky="e",padx=10, pady=10)

direccionLabel=Label(MiFrame, text="Direccion de casa: ")
direccionLabel.grid(row=3, column=0, sticky="e",padx=10, pady=10)

raiz.mainloop()