from tkinter import *

root=Tk()

varOpcion=IntVar()  #Para creear una variable que albergue valores de tipo entero

def Imprimir():
    #print(varOpcion.get())

    if varOpcion.get()==1:
        etiqueta.config(text="Haz elegido masculino")
    
    else:
        etiqueta.config(text="Haz elegido femenimo")

Label(root, text="Genero:").pack()

Radiobutton(root, text="Masculino", variable=varOpcion, value=1, command=Imprimir).pack() #El valor puede ser el que sea
Radiobutton(root, text="Femenino", variable=varOpcion, value=2, command=Imprimir).pack()

etiqueta=Label(root)
etiqueta.pack()



root.mainloop()