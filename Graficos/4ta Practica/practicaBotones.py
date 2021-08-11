from tkinter import *

raiz=Tk()

MiNombre=StringVar()    #Se trata de una cadena de caracteres

MiFrame=Frame(raiz, width=1200, height=600)
MiFrame.pack()

CuadroNombre=Entry(MiFrame, textvariable=MiNombre)  #Asi se asocia el cuadro con la variable
CuadroNombre.grid(row=0, column=1, padx=10, pady=10)
CuadroNombre.config(fg="red", justify="center")

CuadroPass=Entry(MiFrame)
CuadroPass.grid(row=1, column=1, padx=10, pady=10)
CuadroPass.config(show="*")

CuadroApellido=Entry(MiFrame)
CuadroApellido.grid(row=2, column=1, padx=10, pady=10)

CuadroDireccion=Entry(MiFrame)
CuadroDireccion.grid(row=3, column=1, padx=10, pady=10)

TextoComentario=Text(MiFrame, width=16, height=4)
TextoComentario.grid(row=4, column=1, padx=10, pady=10)

scrollVer=Scrollbar(MiFrame, command=TextoComentario.yview) #Para colocar la barra de desplazamiento
scrollVer.grid(row=4, column=2, sticky="nsew")  #Pone la barra de esplazamiento y el nsew es para ajustarla al tamaño del cuadro

TextoComentario.config(yscrollcommand=scrollVer.set)    #Permite que la barra de desplzamiento inidque la posicion 


nombreLabel=Label(MiFrame, text="Nombre: ")
nombreLabel.grid(row=0, column=0, sticky="e", padx=10, pady=10)

passLabel=Label(MiFrame, text="Pasword: ")
passLabel.grid(row=1, column=0, sticky="e", padx=10, pady=10)

apellidoLabel=Label(MiFrame, text="Apelldo: ")
apellidoLabel.grid(row=2, column=0, sticky="e",padx=10, pady=10)

direccionLabel=Label(MiFrame, text="Direccion: ")
direccionLabel.grid(row=3, column=0, sticky="e",padx=10, pady=10)

comentariosLabel=Label(MiFrame, text="Comentarios: ")
comentariosLabel.grid(row=4, column=0, sticky="e",padx=10, pady=10)


def codigoBoton():

    MiNombre.set("Juan")    #Set es para establecer el valor a una variable

BotonEnviar=Button(raiz, text="Enviar", command=codigoBoton)
BotonEnviar.pack()

raiz.mainloop()