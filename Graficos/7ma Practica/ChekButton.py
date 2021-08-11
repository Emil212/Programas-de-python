from tkinter import *

root=Tk()

root.title("Ejemplo")

playa=IntVar()
montana=IntVar()
turismoRural=IntVar()

def opciones():

    opcionEscogida=""

    if(playa.get()==1):
        opcionEscogida+=" playa"
    
    if(montana.get()==1):
        opcionEscogida+=" montana"
    
    if(turismoRural.get()==1):
        opcionEscogida+=" turismo rural"

    textoFinal.config(text=opcionEscogida)

#foto=PhotoImage(file="avion.png")
#Label(root, image=foto).pack()

frame=Frame(root)
frame.pack()

Label(frame, text="Elige destinos", width=50).pack()

Checkbutton(root, text="Playa",variable=playa, onvalue=1, offvalue=0, command=opciones).pack()
Checkbutton(root, text="Montaña", variable=montana, onvalue=1, offvalue=0, command=opciones).pack()
Checkbutton(root, text="Turismo rural", variable=turismoRural, onvalue=1, offvalue=0, command=opciones).pack()

textoFinal=Label(frame)
textoFinal.pack()



root.mainloop()