from tkinter import *

root=Tk()

MiFrame=Frame(root, width=500, height=400)

MiFrame.pack()

miImagen=PhotoImage(file="kono.png")
Label(MiFrame, image=miImagen).place(x=100, y=200)

#Label(MiFrame, text="Hola mundo", fg="red", font=("Comic Sans MS", 18)).place(x=100, y=200)   

#Al empaquetar el label, adapta el contenedor a las dimensiones del label
#Ubica el texto en cualquier lugar de la raiz mediante coordenadas



MiFrame.mainloop()